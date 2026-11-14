from __future__ import annotations

from urllib.parse import urlparse

from app.core.domain.value_objects.value_object import ValueObject

from ..exceptions import InvalidProfileImageException


class ProfileImage(ValueObject):
    def __init__(
        self,
        value: str,
    ) -> None:

        value = value.strip()

        parsed = urlparse(value)

        if not parsed.scheme or not parsed.netloc:
            raise InvalidProfileImageException(value)

        self._value = value

    @property
    def value(self) -> str:

        return self._value

    def __str__(self) -> str:

        return self._value
