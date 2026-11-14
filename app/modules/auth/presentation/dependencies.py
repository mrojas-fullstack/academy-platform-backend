from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import SQLAlchemyUnitOfWork, UnitOfWork, get_session
from app.core.exceptions.authentication import AuthenticationException
from app.modules.auth.application.services.google_identity_verifier import (
    GoogleIdentityVerifier,
)
from app.modules.auth.application.services.token_service import TokenService
from app.modules.auth.domain.entities import Session
from app.modules.auth.domain.repositories import (
    IdentityRepository,
    RefreshTokenRepository,
    SessionRepository,
    UserRepository,
)
from app.modules.auth.domain.value_objects import SessionId
from app.modules.auth.infrastructure.database.repositories import (
    SQLAlchemyIdentityRepository,
    SQLAlchemyRefreshTokenRepository,
    SQLAlchemySessionRepository,
    SQLAlchemyUserRepository,
)

bearer_scheme = HTTPBearer(auto_error=False)


@dataclass(frozen=True, slots=True)
class AuthDependencies:
    user_repository: UserRepository
    identity_repository: IdentityRepository
    session_repository: SessionRepository
    refresh_token_repository: RefreshTokenRepository
    google_identity_verifier: GoogleIdentityVerifier
    token_service: TokenService
    unit_of_work: UnitOfWork


def get_auth_dependencies(
    request: Request,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> AuthDependencies:
    container = request.app.state.context.container

    return AuthDependencies(
        user_repository=SQLAlchemyUserRepository(session=session),
        identity_repository=SQLAlchemyIdentityRepository(session=session),
        session_repository=SQLAlchemySessionRepository(session=session),
        refresh_token_repository=SQLAlchemyRefreshTokenRepository(
            session=session,
        ),
        google_identity_verifier=container.resolve(
            GoogleIdentityVerifier,
        ),
        token_service=container.resolve(
            TokenService,
        ),
        unit_of_work=SQLAlchemyUnitOfWork(session=session),
    )


async def get_current_session(
    dependencies: Annotated[
        AuthDependencies,
        Depends(get_auth_dependencies),
    ],
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(bearer_scheme),
    ],
) -> Session:
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired authentication credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if credentials is None:
        raise unauthorized

    try:
        payload = dependencies.token_service.decode_access_token(
            credentials.credentials,
        )

        session_id = SessionId(UUID(payload["sid"]))
        user_id = payload["sub"]

    except (AuthenticationException, KeyError, TypeError, ValueError):
        raise unauthorized from None

    session = await dependencies.session_repository.get_by_id(
        session_id,
    )

    if session is None or not session.is_active:
        raise unauthorized

    if str(session.user_id.value) != user_id:
        raise unauthorized

    return session
