from __future__ import annotations

import re

from app.core.domain.value_objects.value_object import ValueObject

from ..exceptions import InvalidLocaleException

_PATTERN = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")


class Locale(ValueObject):
    def __init__(
        self,
        value: str,
    ) -> None:

        value = value.strip()

        if not _PATTERN.fullmatch(value):
            raise InvalidLocaleException(value)

        self._value = value

    @property
    def value(self) -> str:

        return self._value

    def __str__(self) -> str:

        return self._value
