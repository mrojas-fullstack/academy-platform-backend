from __future__ import annotations

import re

from .base import ValueObject
from ..exceptions import InvalidEmailException


_EMAIL_REGEX = re.compile(
    r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
)


class Email(ValueObject):

    def __init__(
        self,
        value: str,
    ) -> None:

        value = value.strip().lower()

        if not _EMAIL_REGEX.fullmatch(value):
            raise InvalidEmailException(value)

        self._value = value

    @property
    def value(self) -> str:

        return self._value

    def __str__(self) -> str:

        return self._value