from __future__ import annotations

from uuid import UUID, uuid4

from .base import ValueObject


class EntityId(ValueObject):

    def __init__(
        self,
        value: UUID | None = None,
    ) -> None:

        self._value = value or uuid4()

    @property
    def value(self) -> UUID:

        return self._value

    def __str__(self) -> str:

        return str(self._value)