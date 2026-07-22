from __future__ import annotations

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import EntityId

from .entity import Entity


class AggregateRoot(Entity):

    def __init__(
        self,
        entity_id: EntityId,
    ) -> None:

        super().__init__(entity_id)

        self._domain_events: list[DomainEvent] = []

    @property
    def domain_events(
        self,
    ) -> tuple[DomainEvent, ...]:

        return tuple(self._domain_events)

    def add_domain_event(
        self,
        event: DomainEvent,
    ) -> None:

        self._domain_events.append(event)

    def clear_domain_events(
        self,
    ) -> None:

        self._domain_events.clear()