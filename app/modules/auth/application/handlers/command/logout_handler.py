from __future__ import annotations

from uuid import UUID

from app.core.database import UnitOfWork
from app.core.exceptions.authentication import AuthenticationException
from app.core.messaging.interfaces import CommandHandler
from app.modules.auth.application.commands.logout import LogoutCommand
from app.modules.auth.domain.enums import TokenStatus
from app.modules.auth.domain.repositories import (
    RefreshTokenRepository,
    SessionRepository,
)
from app.modules.auth.domain.value_objects import SessionId


class LogoutHandler(CommandHandler[LogoutCommand, None]):
    def __init__(
        self,
        session_repository: SessionRepository,
        refresh_token_repository: RefreshTokenRepository,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._session_repository = session_repository
        self._refresh_token_repository = refresh_token_repository
        self._unit_of_work = unit_of_work

    async def handle(self, command: LogoutCommand) -> None:
        try:
            session_id = SessionId(UUID(command.session_id))

            session = await self._session_repository.get_by_id(session_id)

            if session is None:
                raise AuthenticationException("Session not found.")

            session.revoke()
            await self._session_repository.update(session)

            refresh_tokens = await self._refresh_token_repository.get_by_session_id(
                session.id,
            )

            for refresh_token in refresh_tokens:
                if refresh_token.status == TokenStatus.ACTIVE:
                    refresh_token.revoke()
                    await self._refresh_token_repository.update(
                        refresh_token,
                    )

            await self._unit_of_work.commit()

        except Exception:
            await self._unit_of_work.rollback()
            raise
