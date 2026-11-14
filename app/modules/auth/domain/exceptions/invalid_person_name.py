from app.core.exceptions import ValidationException


class InvalidPersonNameException(ValidationException):
    def __init__(
        self,
        name: str,
    ) -> None:

        super().__init__(f"'{name}' is not a valid person name.")
