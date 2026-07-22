from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

TId = TypeVar("TId")


class Entity(ABC, Generic[TId]):

    def __init__(
        self,
        id: TId,
    ) -> None:

        self._id = id

    @property
    def id(self) -> TId:
        return self._id

    def __eq__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, Entity):
            return False

        return (
            self.__class__ is other.__class__
            and self.id == other.id
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.__class__,
                self.id,
            )
        )