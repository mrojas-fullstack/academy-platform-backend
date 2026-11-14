from __future__ import annotations

from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from app.core.domain.value_objects.value_object import ValueObject

from ..exceptions import InvalidTimeZoneException


class TimeZone(ValueObject):
    def __init__(
        self,
        value: str,
    ) -> None:

        value = value.strip()

        try:
            ZoneInfo(value)

        except ZoneInfoNotFoundError as ex:
            raise InvalidTimeZoneException(value) from ex

        self._value = value

    @property
    def value(self) -> str:

        return self._value

    def __str__(self) -> str:

        return self._value
