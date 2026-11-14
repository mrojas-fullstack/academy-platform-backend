from collections.abc import Callable
from typing import Any

from .exceptions import (
    DependencyAlreadyRegisteredError,
    DependencyNotRegisteredError,
)
from .lifetime import ServiceLifetime
from .provider import ServiceProvider
from .service_descriptor import ServiceDescriptor
from .types import Provider


class Container:
    def __init__(self) -> None:

        self._services: dict[type, ServiceDescriptor] = {}

        self._provider = ServiceProvider(self)

    def register(
        self,
        interface: type,
        provider: Provider | None = None,
        lifetime: ServiceLifetime = ServiceLifetime.TRANSIENT,
    ) -> None:

        if interface in self._services:
            raise DependencyAlreadyRegisteredError(
                f"{interface.__name__} has already been registered."
            )

        self._services[interface] = ServiceDescriptor(
            service_type=interface,
            provider=provider or interface,
            lifetime=lifetime,
        )

    def register_instance(
        self,
        interface: type,
        instance: Any,
    ) -> None:

        if interface in self._services:
            raise DependencyAlreadyRegisteredError(
                f"{interface.__name__} has already been registered."
            )

        self._services[interface] = ServiceDescriptor(
            service_type=interface,
            provider=lambda: instance,
            lifetime=ServiceLifetime.SINGLETON,
            instance=instance,
        )

    def register_factory(
        self,
        interface: type,
        factory: Callable[[], Any],
        lifetime: ServiceLifetime = ServiceLifetime.TRANSIENT,
    ) -> None:

        self.register(
            interface=interface,
            provider=factory,
            lifetime=lifetime,
        )

    def resolve(
        self,
        interface: type,
    ) -> Any:

        descriptor = self._services.get(interface)

        if descriptor is None:
            raise DependencyNotRegisteredError(f"{interface.__name__} has not been registered.")

        return self._provider.provide(descriptor)

    def contains(
        self,
        interface: type,
    ) -> bool:

        return interface in self._services
