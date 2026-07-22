from __future__ import annotations

from datetime import UTC, datetime
from typing import Generic, TypeVar

from .aggregate_root import AggregateRoot

TId = TypeVar("TId")


class AuditableAggregateRoot(
    AggregateRoot[TId],
    Generic[TId],
):

    def __init__(
        self,
        id: TId,
    ) -> None:

        super().__init__(id)

        now = datetime.now(UTC)

        self._created_at = now
        self._updated_at = now

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def touch(self) -> None:
        """
        Updates the modification timestamp.
        """

        self._updated_at = datetime.now(UTC)