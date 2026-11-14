from app.core.messaging import MessageBus

from .domain_event import DomainEvent


class DomainEventDispatcher:
    def __init__(
        self,
        bus: MessageBus,
    ) -> None:

        self._bus = bus

    async def dispatch(
        self,
        *events: DomainEvent,
    ) -> None:

        for event in events:
            await self._bus.publish(event)
