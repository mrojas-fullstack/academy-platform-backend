from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import SQLAlchemyUnitOfWork, UnitOfWork, get_session
from app.modules.auth.application.services.google_identity_verifier import (
    GoogleIdentityVerifier,
)
from app.modules.auth.application.services.token_service import TokenService
from app.modules.auth.domain.repositories import (
    IdentityRepository,
    RefreshTokenRepository,
    SessionRepository,
    UserRepository,
)
from app.modules.auth.infrastructure.database.repositories import (
    SQLAlchemyIdentityRepository,
    SQLAlchemyRefreshTokenRepository,
    SQLAlchemySessionRepository,
    SQLAlchemyUserRepository,
)


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
