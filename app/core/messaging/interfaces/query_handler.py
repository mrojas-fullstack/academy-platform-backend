from .handler import Handler
from .query import Query


class QueryHandler[TQuery: Query, TResult](
    Handler[TQuery, TResult],
):
    """
    Base class for query handlers.
    """

    pass
