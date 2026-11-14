from dataclasses import dataclass

from .lifetime import ServiceLifetime
from .types import Provider, ServiceType


@dataclass(slots=True)
class ServiceDescriptor:
    service_type: ServiceType

    provider: Provider

    lifetime: ServiceLifetime

    instance: object | None = None
