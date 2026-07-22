from .domain import DomainException


class ConflictException(DomainException):
    """
    Base exception for business conflicts.
    """
