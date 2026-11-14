from __future__ import annotations

from datetime import UTC, datetime, timedelta

import jwt

from app.core.settings.auth import AuthSettings
from app.modules.auth.application.services.token_service import TokenService
from app.modules.auth.domain.value_objects import SessionId, UserId


class JwtTokenService(TokenService):
    def __init__(
        self,
        settings: AuthSettings,
    ) -> None:
        self._settings = settings

    def create_access_token(
        self,
        user_id: UserId,
        session_id: SessionId,
    ) -> str:
        now = datetime.now(UTC)
        expires_at = now + timedelta(
            minutes=self._settings.JWT_EXPIRE_MINUTES,
        )

        payload = {
            "sub": str(user_id.value),
            "sid": str(session_id.value),
            "iat": now,
            "exp": expires_at,
            "type": "access",
        }

        return jwt.encode(
            payload,
            self._settings.JWT_SECRET,
            algorithm=self._settings.JWT_ALGORITHM,
        )

    def decode_access_token(
        self,
        token: str,
    ) -> dict[str, str]:
        payload = jwt.decode(
            token,
            self._settings.JWT_SECRET,
            algorithms=[self._settings.JWT_ALGORITHM],
        )

        if payload.get("type") != "access":
            raise jwt.InvalidTokenError("Invalid token type.")

        return {
            "sub": str(payload["sub"]),
            "sid": str(payload["sid"]),
        }
