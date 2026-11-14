from __future__ import annotations

from collections.abc import AsyncGenerator

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import SQLAlchemyUnitOfWork, get_session
from app.modules.auth.application.commands import (
    GoogleLoginCommand,
    RefreshTokenCommand,
    RegisterUserCommand,
)
from app.modules.auth.application.handlers.command import (
    GoogleLoginHandler,
    RefreshTokenHandler,
    RegisterUserHandler,
)
from app.modules.auth.infrastructure.database.repositories import (
    SQLAlchemyUserRepository,
)
from app.modules.auth.presentation.dependencies import (
    AuthDependencies,
    get_auth_dependencies,
)
from app.modules.auth.presentation.requests.google_login_request import (
    GoogleLoginRequest,
)
from app.modules.auth.presentation.requests.refresh_token_request import (
    RefreshTokenRequest,
)
from app.modules.auth.presentation.requests.register_request import (
    RegisterRequest,
)
from app.modules.auth.presentation.responses.google_login_response import (
    GoogleLoginResponse,
)
from app.modules.auth.presentation.responses.refresh_token_response import (
    RefreshTokenResponse,
)
from app.modules.auth.presentation.responses.register_response import (
    RegisterResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


async def get_register_user_handler(
    session: AsyncSession = Depends(get_session),
) -> AsyncGenerator[RegisterUserHandler]:
    repository = SQLAlchemyUserRepository(
        session=session,
    )

    unit_of_work = SQLAlchemyUnitOfWork(
        session=session,
    )

    yield RegisterUserHandler(
        user_repository=repository,
        unit_of_work=unit_of_work,
    )


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    body: RegisterRequest,
    handler: RegisterUserHandler = Depends(get_register_user_handler),
) -> RegisterResponse:

    user_id = await handler.handle(
        RegisterUserCommand(
            email=body.email,
            first_name=body.first_name,
            last_name=body.last_name,
            locale=body.locale,
            time_zone=body.time_zone,
            profile_image=body.profile_image,
        )
    )

    return RegisterResponse(
        id=str(user_id.value),
        message="User registered successfully.",
    )


@router.post(
    "/google",
    response_model=GoogleLoginResponse,
    status_code=status.HTTP_200_OK,
)
async def google_login(
    body: GoogleLoginRequest,
    dependencies: AuthDependencies = Depends(get_auth_dependencies),
) -> GoogleLoginResponse:
    handler = GoogleLoginHandler(
        user_repository=dependencies.user_repository,
        identity_repository=dependencies.identity_repository,
        session_repository=dependencies.session_repository,
        refresh_token_repository=dependencies.refresh_token_repository,
        google_identity_verifier=dependencies.google_identity_verifier,
        token_service=dependencies.token_service,
        unit_of_work=dependencies.unit_of_work,
    )

    tokens = await handler.handle(
        GoogleLoginCommand(
            credential=body.credential,
            locale=body.locale,
            time_zone=body.time_zone,
        )
    )

    return GoogleLoginResponse(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
    )


@router.post(
    "/refresh",
    response_model=RefreshTokenResponse,
    status_code=status.HTTP_200_OK,
)
async def refresh_token(
    body: RefreshTokenRequest,
    dependencies: AuthDependencies = Depends(get_auth_dependencies),
) -> RefreshTokenResponse:
    handler = RefreshTokenHandler(
        refresh_token_repository=dependencies.refresh_token_repository,
        session_repository=dependencies.session_repository,
        token_service=dependencies.token_service,
        unit_of_work=dependencies.unit_of_work,
    )

    tokens = await handler.handle(
        RefreshTokenCommand(
            refresh_token=body.refresh_token,
        )
    )

    return RefreshTokenResponse(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
    )
