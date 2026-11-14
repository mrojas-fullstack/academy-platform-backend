from __future__ import annotations

import inspect
from types import ModuleType

from app.core.messaging.interfaces.command_handler import CommandHandler
from app.core.messaging.interfaces.event_handler import EventHandler
from app.core.messaging.interfaces.query_handler import QueryHandler


class Reflection:
    _HANDLER_TYPES: tuple[type, ...] = (
        CommandHandler,
        QueryHandler,
        EventHandler,
    )

    @staticmethod
    def get_classes(
        module: ModuleType,
    ) -> list[type]:

        return [
            obj
            for _, obj in inspect.getmembers(
                module,
                inspect.isclass,
            )
            if obj.__module__ == module.__name__
        ]

    @classmethod
    def is_handler(
        cls,
        obj: type,
    ) -> bool:

        return obj not in cls._HANDLER_TYPES and issubclass(
            obj,
            cls._HANDLER_TYPES,
        )

    @staticmethod
    def inherits_from(
        handler: type,
        handler_type: type,
    ) -> bool:

        return issubclass(
            handler,
            handler_type,
        )

    @staticmethod
    def get_message_type(
        handler: type,
        handler_type: type,
    ) -> type:

        for base in getattr(
            handler,
            "__orig_bases__",
            (),
        ):
            origin = getattr(
                base,
                "__origin__",
                None,
            )

            if origin is handler_type:
                arguments = getattr(
                    base,
                    "__args__",
                    (),
                )

                if not arguments:
                    break

                message_type = arguments[0]

                if isinstance(message_type, type):
                    return message_type

        raise TypeError(f"Could not determine message type for {handler.__name__}.")
