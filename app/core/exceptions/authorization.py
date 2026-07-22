from .domain import DomainException


class AuthorizationException(DomainException):
    """
    Base exception for authorization failures.
    """