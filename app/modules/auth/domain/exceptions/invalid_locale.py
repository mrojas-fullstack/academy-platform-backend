from app.core.exceptions import ValidationException


class InvalidLocaleException(ValidationException):
    def __init__(
        self,
        locale: str,
    ) -> None:

        super().__init__(f"'{locale}' is not a valid locale.")
