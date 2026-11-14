from .command import Command
from .handler import Handler


class CommandHandler[TCommand: Command, TResult](
    Handler[TCommand, TResult],
):
    """
    Base class for command handlers.
    """

    pass
