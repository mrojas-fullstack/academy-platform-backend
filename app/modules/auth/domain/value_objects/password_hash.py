from __future__ import annotations

from app.core.domain.value_objects.value_object import ValueObject


class PasswordHash(ValueObject):
    def __init__(self, value: str) -> None:
        if not value or not value.strip() or any(char.isspace() for char in value):
            raise ValueError("Password hash cannot be empty or contain whitespace.")

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self._value
