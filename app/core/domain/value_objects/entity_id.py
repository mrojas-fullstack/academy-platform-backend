from __future__ import annotations

from typing import Self
from uuid import UUID, uuid4

from .value_object import ValueObject


class EntityId(ValueObject):
    def __init__(
        self,
        value: UUID,
    ) -> None:

        self._value = value

    @classmethod
    def new(cls) -> Self:
        """
        Creates a new unique EntityId.
        """

        return cls(uuid4())

    @classmethod
    def from_string(
        cls,
        value: str,
    ) -> Self:
        """
        Reconstructs an EntityId from its string representation.
        """

        return cls(UUID(value))

    @property
    def value(self) -> UUID:

        return self._value

    def __str__(self) -> str:

        return str(self._value)

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}({self._value})"
