from app.core.exceptions import ValidationException


class InvalidTimeZoneException(ValidationException):
    def __init__(
        self,
        time_zone: str,
    ) -> None:

        super().__init__(f"'{time_zone}' is not a valid time zone.")
