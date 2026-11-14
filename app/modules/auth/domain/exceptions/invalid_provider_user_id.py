from app.core.exceptions import ValidationException


class InvalidProviderUserIdException(ValidationException):
    def __init__(
        self,
        provider_user_id: str,
    ) -> None:

        super().__init__("Provider user id is invalid.")
