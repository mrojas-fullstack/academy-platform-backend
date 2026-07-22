from app.core.messaging.exceptions import (
    HandlerNotFoundError,
    InvalidHandlerError,
    MessageAlreadyRegisteredError,
)
from .interfaces.command_handler import CommandHandler
from .interfaces.event_handler import EventHandler
from .interfaces.query_handler import QueryHandler
from .reflection import Reflection


class MessageRegistry:

    def __init__(self) -> None:

        self._commands: dict[type, type] = {}

        self._queries: dict[type, type] = {}

        self._events: dict[type, list[type]] = {}

    def register(
        self,
        handler: type,
    ) -> None:

        if Reflection.inherits_from(handler, CommandHandler):

            message = Reflection.get_message_type(
                handler,
                CommandHandler,
            )

            if message in self._commands:
                raise MessageAlreadyRegisteredError(
                    f"{message.__name__} already registered."
                )

            self._commands[message] = handler
            return

        if Reflection.inherits_from(handler, QueryHandler):

            message = Reflection.get_message_type(
                handler,
                QueryHandler,
            )

            if message in self._queries:
                raise MessageAlreadyRegisteredError(
                    f"{message.__name__} already registered."
                )

            self._queries[message] = handler
            return

        if Reflection.inherits_from(handler, EventHandler):

            message = Reflection.get_message_type(
                handler,
                EventHandler,
            )

            self._events.setdefault(
                message,
                [],
            ).append(handler)

            return

        raise InvalidHandlerError(
            f"{handler.__name__} is not a valid handler."
        )

    def get_command_handler(
        self,
        message: type,
    ) -> type:

        handler = self._commands.get(message)

        if handler is None:
            raise HandlerNotFoundError(
                f"No handler registered for {message.__name__}."
            )

        return handler

    def get_query_handler(
        self,
        message: type,
    ) -> type:

        handler = self._queries.get(message)

        if handler is None:
            raise HandlerNotFoundError(
                f"No handler registered for {message.__name__}."
            )

        return handler

    def get_event_handlers(
        self,
        message: type,
    ) -> list[type]:

        return self._events.get(
            message,
            [],
        )

    def contains_command(
        self,
        message: type,
    ) -> bool:

        return message in self._commands

    def contains_query(
        self,
        message: type,
    ) -> bool:

        return message in self._queries

    def contains_event(
        self,
        message: type,
    ) -> bool:

        return message in self._events