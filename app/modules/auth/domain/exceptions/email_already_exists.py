from app.core.exceptions import ConflictException


class EmailAlreadyExistsException(ConflictException):

    def __init__(
        self,
        email: str,
    ) -> None:

        super().__init__(
            f"The email '{email}' is already registered."
        )