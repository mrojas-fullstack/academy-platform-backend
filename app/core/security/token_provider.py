from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Any


class TokenProvider(ABC):
    """
    Contract for access and refresh token providers.
    """

    @abstractmethod
    def generate_access_token(
        self,
        subject: str,
        claims: dict[str, Any] | None = None,
        expires_in: timedelta | None = None,
    ) -> str:
        """
        Generates an access token.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_refresh_token(
        self,
        subject: str,
        claims: dict[str, Any] | None = None,
        expires_in: timedelta | None = None,
    ) -> str:
        """
        Generates a refresh token.
        """
        raise NotImplementedError

    @abstractmethod
    def verify(
        self,
        token: str,
    ) -> dict[str, Any]:
        """
        Verifies a token and returns its payload.
        """
        raise NotImplementedError
