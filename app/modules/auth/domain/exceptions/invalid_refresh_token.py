from app.core.exceptions import AuthenticationException


class InvalidRefreshTokenException(AuthenticationException):
    def __init__(self, refresh_token: str) -> None:
        super().__init__(f"Invalid refresh token: {refresh_token}")
