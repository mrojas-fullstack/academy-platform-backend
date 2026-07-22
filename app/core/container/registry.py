from functools import lru_cache

from .container import Container


@lru_cache(maxsize=1)
def get_container() -> Container:
    return Container()