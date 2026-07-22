class MessagingError(Exception):
    """Base messaging exception."""


class InvalidMessageError(MessagingError):
    """Raised when a message type is invalid."""


class InvalidHandlerError(MessagingError):
    """Raised when a handler type is invalid."""


class HandlerNotFoundError(MessagingError):
    """Raised when no handler is registered."""


class MultipleHandlersFoundError(MessagingError):
    """Raised when multiple handlers are found for a command or query."""


class MessageAlreadyRegisteredError(MessagingError):
    """Raised when a message is registered more than once."""