from __future__ import annotations

import hashlib
import secrets
from datetime import UTC, datetime, timedelta

from app.core.database import UnitOfWork
from app.core.messaging.interfaces import CommandHandler
from app.modules.auth.application.commands import RefreshTokenCommand
from app.modules.auth.application.services.token_service import TokenService
from app.modules.auth.domain.entities import RefreshToken
from app.modules.auth.domain.enums import TokenStatus
from app.modules.auth.domain.exceptions.invalid_refresh_token import InvalidRefreshTokenException
from app.modules.auth.domain.repositories import (
    RefreshTokenRepository,
    SessionRepository,
)
from app.modules.auth.domain.value_objects import (
    RefreshTokenHash,
    RefreshTokenId,
)


class RefreshTokenHandler(
    CommandHandler[RefreshTokenCommand, dict[str, str]],
):
    REFRESH_TOKEN_EXPIRE_DAYS = 30

    def __init__(
        self,
        refresh_token_repository: RefreshTokenRepository,
        session_repository: SessionRepository,
        token_service: TokenService,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._refresh_token_repository = refresh_token_repository
        self._session_repository = session_repository
        self._token_service = token_service
        self._unit_of_work = unit_of_work

    async def handle(
        self,
        command: RefreshTokenCommand,
    ) -> dict[str, str]:
        token_hash = RefreshTokenHash(
            hashlib.sha256(
                command.refresh_token.encode(),
            ).hexdigest(),
        )

        stored_token = await self._refresh_token_repository.get_by_hash(
            token_hash,
        )

        if stored_token is None:
            raise InvalidRefreshTokenException("Stored_token is None.")

        session = await self._session_repository.get_by_id(
            stored_token.session_id,
        )

        if stored_token.status is TokenStatus.ROTATED:
            if session is not None:
                session.revoke()
                await self._session_repository.update(session)

            tokens = await self._refresh_token_repository.get_by_session_id(
                stored_token.session_id,
            )

            for token in tokens:
                if token.status is TokenStatus.ACTIVE:
                    token.revoke()
                    await self._refresh_token_repository.update(token)

            await self._unit_of_work.commit()

            raise InvalidRefreshTokenException(
                "Refresh token reuse detected. Session revoked.",
            )

        if not stored_token.is_active or session is None or not session.is_active:
            raise InvalidRefreshTokenException("Invalid or expired refresh token.")

        now = datetime.now(UTC)

        stored_token.rotate()
        await self._refresh_token_repository.update(stored_token)

        raw_refresh_token = secrets.token_urlsafe(64)

        new_refresh_token = RefreshToken(
            refresh_token_id=RefreshTokenId.new(),
            session_id=stored_token.session_id,
            token_hash=RefreshTokenHash(
                hashlib.sha256(
                    raw_refresh_token.encode(),
                ).hexdigest(),
            ),
            status=TokenStatus.ACTIVE,
            created_at=now,
            expires_at=now
            + timedelta(
                days=self.REFRESH_TOKEN_EXPIRE_DAYS,
            ),
        )

        await self._refresh_token_repository.add(new_refresh_token)

        session.touch(now)
        await self._session_repository.update(session)

        access_token = self._token_service.create_access_token(
            user_id=session.user_id,
            session_id=session.id,
        )

        await self._unit_of_work.commit()

        return {
            "access_token": access_token,
            "refresh_token": raw_refresh_token,
        }
