from app.core.exceptions import ConflictException


class IdentityAlreadyLinkedException(ConflictException):
    def __init__(
        self,
        provider: str,
        provider_user_id: str,
    ) -> None:

        super().__init__(f"Identity '{provider}:{provider_user_id}' is already linked.")
