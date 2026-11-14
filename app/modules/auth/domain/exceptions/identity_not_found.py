from app.core.exceptions import NotFoundException


class IdentityNotFoundException(NotFoundException):
    def __init__(
        self,
        provider: str,
        provider_user_id: str,
    ) -> None:

        super().__init__(f"Identity '{provider}:{provider_user_id}' was not found.")
