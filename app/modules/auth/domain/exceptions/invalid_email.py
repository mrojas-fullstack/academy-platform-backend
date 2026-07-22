from app.core.exceptions import ValidationException


class InvalidEmailException(ValidationException):

    def __init__(
        self,
        email: str,
    ) -> None:

        super().__init__(
            f"'{email}' is not a valid email address."
        )