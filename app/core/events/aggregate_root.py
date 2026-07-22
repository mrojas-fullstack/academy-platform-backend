from __future__ import annotations

from typing import Generic, TypeVar

from .domain_event import DomainEvent
from .entity import Entity

TId = TypeVar("TId")


class AggregateRoot(
    Entity[TId],
    Generic[TId],
):

    def __init__(
        self,
        id: TId,
    ) -> None:

        super().__init__(id)

        self._events: list[DomainEvent] = []

    @property
    def events(
        self,
    ) -> tuple[DomainEvent, ...]:

        return tuple(self._events)

    def add_event(
        self,
        event: DomainEvent,
    ) -> None:

        self._events.append(event)

    def clear_events(
        self,
    ) -> None:

        self._events.clear()