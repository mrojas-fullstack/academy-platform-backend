from app.core.exceptions import AuthenticationException


class InvalidGoogleCredentialException(AuthenticationException):
    def __init__(self) -> None:
        super().__init__("Invalid Google credential.")
