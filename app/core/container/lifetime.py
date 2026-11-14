from enum import Enum, auto


class ServiceLifetime(Enum):
    SINGLETON = auto()

    TRANSIENT = auto()

    SCOPED = auto()

    def is_singleton(self) -> bool:

        return self is ServiceLifetime.SINGLETON
