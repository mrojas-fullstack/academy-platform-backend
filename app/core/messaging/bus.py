from typing import Any

from app.core.container import Container

from .registry import MessageRegistry


class MessageBus:

    def __init__(
        self,
        registry: MessageRegistry,
        container: Container,
    ) -> None:

        self._registry = registry
        self._container = container

    async def send(
        self,
        command: Any,
    ) -> Any:

        handler_type = self._registry.get_command_handler(
            type(command),
        )

        handler = self._container.resolve(
            handler_type,
        )

        return await handler.handle(command)

    async def query(
        self,
        query: Any,
    ) -> Any:

        handler_type = self._registry.get_query_handler(
            type(query),
        )

        handler = self._container.resolve(
            handler_type,
        )

        return await handler.handle(query)

    async def publish(
        self,
        event: Any,
    ) -> None:

        handler_types = self._registry.get_event_handlers(
            type(event),
        )

        for handler_type in handler_types:

            handler = self._container.resolve(
                handler_type,
            )

            await handler.handle(event)