from collections.abc import Callable
from typing import Any

type ServiceType = type[Any]

type Factory = Callable[[], Any]

type Provider = ServiceType | Factory
