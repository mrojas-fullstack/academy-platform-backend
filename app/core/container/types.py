from collections.abc import Callable
from typing import Any, TypeAlias

ServiceType: TypeAlias = type[Any]

Factory: TypeAlias = Callable[[], Any]

Provider: TypeAlias = ServiceType | Factory