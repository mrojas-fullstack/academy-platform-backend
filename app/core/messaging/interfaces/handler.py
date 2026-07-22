from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .message import Message

TMessage = TypeVar("TMessage", bound=Message)
TResult = TypeVar("TResult")


class Handler(
    ABC,
    Generic[TMessage, TResult],
):
    """
    Base interface for all message handlers.
    """

    @abstractmethod
    async def handle(
        self,
        message: TMessage,
    ) -> TResult:
        ...