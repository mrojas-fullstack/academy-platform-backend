from typing import Generic, TypeVar

from .event import Event
from .handler import Handler

TEvent = TypeVar(
    "TEvent",
    bound=Event,
)


class EventHandler(
    Handler[TEvent, None],
    Generic[TEvent],
):
    """
    Base class for event handlers.
    """

    pass