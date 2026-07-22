from typing import Generic, TypeVar

from .command import Command
from .handler import Handler, TResult

TCommand = TypeVar(
    "TCommand",
    bound=Command,
)


class CommandHandler(
    Handler[TCommand, TResult],
    Generic[TCommand, TResult],
):
    """
    Base class for command handlers.
    """

    pass