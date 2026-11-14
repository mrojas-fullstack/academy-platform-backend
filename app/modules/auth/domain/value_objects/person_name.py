from __future__ import annotations

from app.core.domain.value_objects.value_object import ValueObject

from ..exceptions import InvalidPersonNameException


class PersonName(ValueObject):
    MAX_LENGTH = 100

    def __init__(
        self,
        value: str,
    ) -> None:

        value = value.strip()

        if not value:
            raise InvalidPersonNameException(value)

        if len(value) > self.MAX_LENGTH:
            raise InvalidPersonNameException(value)

        self._value = value

    @property
    def value(self) -> str:

        return self._value

    def __str__(self) -> str:

        return self._value
