from __future__ import annotations

from google.auth.exceptions import GoogleAuthError
from google.auth.transport import requests
from google.oauth2 import id_token

from app.core.settings.google import GoogleSettings
from app.modules.auth.application.dto import GoogleIdentity
from app.modules.auth.application.services.google_identity_verifier import (
    GoogleIdentityVerifier,
)
from app.modules.auth.domain.exceptions import (
    InvalidGoogleCredentialException,
)


class GoogleIdentityTokenVerifier(GoogleIdentityVerifier):
    def __init__(
        self,
        settings: GoogleSettings,
    ) -> None:
        self._settings = settings

    async def verify(
        self,
        credential: str,
    ) -> GoogleIdentity:

        try:
            payload = id_token.verify_oauth2_token(
                credential,
                requests.Request(),
                self._settings.GOOGLE_CLIENT_ID,
            )  # type: ignore[no-untyped-call]
        except GoogleAuthError as exc:
            raise InvalidGoogleCredentialException() from exc
        except ValueError as exc:
            raise InvalidGoogleCredentialException() from exc

        return GoogleIdentity(
            provider_user_id=payload["sub"],
            email=payload["email"],
            first_name=payload.get("given_name", ""),
            last_name=payload.get("family_name", ""),
            profile_image=payload.get("picture"),
            email_verified=payload.get("email_verified", False),
        )
