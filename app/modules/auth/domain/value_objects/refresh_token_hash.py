from __future__ import annotations

from app.core.domain.value_objects.value_object import ValueObject


class RefreshTokenHash(ValueObject):
    def __init__(
        self,
        value: str,
    ) -> None:
        normalized_value = value.strip().lower()

        if len(normalized_value) != 64:
            raise ValueError("Refresh token hash must contain 64 hexadecimal characters.")

        try:
            int(normalized_value, 16)
        except ValueError as exc:
            raise ValueError("Refresh token hash must be hexadecimal.") from exc

        self._value = normalized_value

    @property
    def value(self) -> str:
        return self._value
