from typing import Generic, TypeVar

from .query import Query
from .handler import Handler, TResult

TQuery = TypeVar(
    "TQuery",
    bound=Query,
)


class QueryHandler(
    Handler[TQuery, TResult],
    Generic[TQuery, TResult],
):
    """
    Base class for query handlers.
    """

    pass