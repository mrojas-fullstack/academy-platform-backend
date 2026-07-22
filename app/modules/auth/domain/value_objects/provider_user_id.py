from __future__ import annotations

from .base import ValueObject
from ..exceptions import InvalidProviderUserIdException


class ProviderUserId(ValueObject):

    def __init__(
        self,
        value: str,
    ) -> None:

        value = value.strip()

        if not value:
            raise InvalidProviderUserIdException(value)

        self._value = value

    @property
    def value(self) -> str:

        return self._value

    def __str__(self) -> str:

        return self._value