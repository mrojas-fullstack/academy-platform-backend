from app.core.exceptions import NotFoundException


class UserNotFoundException(NotFoundException):

    def __init__(
        self,
        user_id: str,
    ) -> None:

        super().__init__(
            f"User '{user_id}' was not found."
        )