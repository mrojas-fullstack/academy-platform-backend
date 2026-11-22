from app.core.exceptions import ValidationException


class InvalidLoginIdentifierException(ValidationException):
    def __init__(self, identifier: str) -> None:
        super().__init__(f"'{identifier}' is not a valid login identifier.")
