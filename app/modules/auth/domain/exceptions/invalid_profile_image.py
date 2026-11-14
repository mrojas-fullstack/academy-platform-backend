from app.core.exceptions import ValidationException


class InvalidProfileImageException(ValidationException):
    def __init__(
        self,
        image: str,
    ) -> None:

        super().__init__(f"'{image}' is not a valid profile image URL.")
