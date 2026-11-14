from __future__ import annotations

import hashlib
import secrets
from datetime import UTC, datetime, timedelta

from app.core.database import UnitOfWork
from app.core.messaging.interfaces import CommandHandler
from app.modules.auth.application.commands import GoogleLoginCommand
from app.modules.auth.application.services.google_identity_verifier import (
    GoogleIdentityVerifier,
)
from app.modules.auth.application.services.token_service import TokenService
from app.modules.auth.domain.entities import Identity, RefreshToken, Session
from app.modules.auth.domain.enums import (
    IdentityProvider,
    SessionStatus,
    TokenStatus,
)
from app.modules.auth.domain.exceptions import (
    EmailAlreadyExistsException,
    InvalidGoogleCredentialException,
)
from app.modules.auth.domain.factories import UserFactory
from app.modules.auth.domain.repositories import (
    IdentityRepository,
    RefreshTokenRepository,
    SessionRepository,
    UserRepository,
)
from app.modules.auth.domain.value_objects import (
    Email,
    IdentityId,
    Locale,
    PersonName,
    ProfileImage,
    ProviderUserId,
    RefreshTokenHash,
    RefreshTokenId,
    SessionId,
    TimeZone,
)


class GoogleLoginHandler(
    CommandHandler[GoogleLoginCommand, dict[str, str]],
):
    REFRESH_TOKEN_EXPIRE_DAYS = 30
    SESSION_EXPIRE_DAYS = 30

    def __init__(
        self,
        user_repository: UserRepository,
        identity_repository: IdentityRepository,
        session_repository: SessionRepository,
        refresh_token_repository: RefreshTokenRepository,
        google_identity_verifier: GoogleIdentityVerifier,
        token_service: TokenService,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._user_repository = user_repository
        self._identity_repository = identity_repository
        self._session_repository = session_repository
        self._refresh_token_repository = refresh_token_repository
        self._google_identity_verifier = google_identity_verifier
        self._token_service = token_service
        self._unit_of_work = unit_of_work

    async def handle(
        self,
        command: GoogleLoginCommand,
    ) -> dict[str, str]:
        try:
            google_identity = await self._google_identity_verifier.verify(
                command.credential,
            )

            if not google_identity.email_verified:
                raise InvalidGoogleCredentialException()

            provider_user_id = ProviderUserId(
                google_identity.provider_user_id,
            )

            identity = await self._identity_repository.get_by_provider(
                IdentityProvider.GOOGLE,
                provider_user_id,
            )

            if identity is None:
                email = Email(google_identity.email)

                if await self._user_repository.exists_by_email(email):
                    raise EmailAlreadyExistsException(email.value)

                user = UserFactory.register(
                    email=email,
                    first_name=PersonName(google_identity.first_name),
                    last_name=PersonName(google_identity.last_name),
                    locale=Locale(command.locale),
                    time_zone=TimeZone(command.time_zone),
                    profile_image=(
                        ProfileImage(google_identity.profile_image)
                        if google_identity.profile_image
                        else None
                    ),
                )

                await self._user_repository.add(user)

                identity = Identity(
                    identity_id=IdentityId.new(),
                    user_id=user.id,
                    provider=IdentityProvider.GOOGLE,
                    provider_user_id=provider_user_id,
                    provider_email=email,
                    verified=True,
                )

                await self._identity_repository.add(identity)

                user_id = user.id

            else:
                user_id = identity.user_id

                existing_user = await self._user_repository.get_by_id(user_id)

                if existing_user is None:
                    raise InvalidGoogleCredentialException()

            now = datetime.now(UTC)

            session_id = SessionId.new()

            session = Session(
                session_id=session_id,
                user_id=user_id,
                status=SessionStatus.ACTIVE,
                created_at=now,
                expires_at=now
                + timedelta(
                    days=self.SESSION_EXPIRE_DAYS,
                ),
                last_activity_at=now,
            )

            await self._session_repository.add(session)

            raw_refresh_token = secrets.token_urlsafe(64)

            refresh_token = RefreshToken(
                refresh_token_id=RefreshTokenId.new(),
                session_id=session_id,
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

            await self._refresh_token_repository.add(refresh_token)

            access_token = self._token_service.create_access_token(
                user_id=user_id,
                session_id=session_id,
            )

            await self._unit_of_work.commit()

            return {
                "access_token": access_token,
                "refresh_token": raw_refresh_token,
            }

        except Exception:
            await self._unit_of_work.rollback()
            raise
