from abc import ABC, abstractmethod

from .message import Message


class Handler[TMessage: Message, TResult](ABC):
    """
    Base interface for all message handlers.
    """

    @abstractmethod
    async def handle(
        self,
        message: TMessage,
    ) -> TResult: ...
