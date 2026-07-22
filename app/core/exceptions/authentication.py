from .domain import DomainException


class AuthenticationException(DomainException):
    """
    Base exception for authentication failures.
    """