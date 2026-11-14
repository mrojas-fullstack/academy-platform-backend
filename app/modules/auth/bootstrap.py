from __future__ import annotations

from fastapi import FastAPI

from app.core.container import Container
from app.core.settings.auth import AuthSettings
from app.core.settings.google import GoogleSettings
from app.modules.auth.application.services.google_identity_verifier import (
    GoogleIdentityVerifier,
)
from app.modules.auth.application.services.token_service import TokenService
from app.modules.auth.infrastructure.google.google_identity_verifier import (
    GoogleIdentityTokenVerifier,
)
from app.modules.auth.infrastructure.jwt.jwt_token_service import (
    JwtTokenService,
)
from app.modules.auth.presentation.routes.auth_routes import router


def register_services(container: Container) -> None:
    google_settings = GoogleSettings()
    auth_settings = AuthSettings()

    container.register_instance(
        GoogleIdentityVerifier,
        GoogleIdentityTokenVerifier(google_settings),
    )

    container.register_instance(
        TokenService,
        JwtTokenService(auth_settings),
    )


def register_routes(app: FastAPI) -> None:
    app.include_router(router)
