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

        return (
            obj not in cls._HANDLER_TYPES
            and issubclass(
                obj,
                cls._HANDLER_TYPES,
            )
        )