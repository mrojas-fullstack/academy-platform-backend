from __future__ import annotations

from abc import ABC, abstractmethod

from app.modules.auth.domain.value_objects import SessionId, UserId


class TokenService(ABC):
    @abstractmethod
    def create_access_token(
        self,
        user_id: UserId,
        session_id: SessionId,
    ) -> str:
        """Create an access token for an authenticated session."""
        raise NotImplementedError

    @abstractmethod
    def decode_access_token(
        self,
        token: str,
    ) -> dict[str, str]:
        """Decode and validate an access token."""
        raise NotImplementedError
