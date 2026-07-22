from .domain import DomainException


class NotFoundException(DomainException):
    """
    Base exception for resources not found.
    """
