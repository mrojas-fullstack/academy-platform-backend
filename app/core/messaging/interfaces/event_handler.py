from .event import Event
from .handler import Handler


class EventHandler[TEvent: Event](
    Handler[TEvent, None],
):
    """
    Base class for event handlers.
    """

    pass
