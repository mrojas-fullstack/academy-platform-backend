from __future__ import annotations

import inspect
from typing import TYPE_CHECKING, Any

from .exceptions import DependencyNotRegisteredError
from .service_descriptor import ServiceDescriptor

if TYPE_CHECKING:
    from .container import Container


class ServiceProvider:

    def __init__(
        self,
        container: Container,
    ) -> None:

        self._container = container

    def provide(
        self,
        descriptor: ServiceDescriptor,
    ) -> Any:

        if descriptor.instance is not None:
            return descriptor.instance

        provider = descriptor.provider

        if inspect.isclass(provider):
            instance = self._create(provider)
        else:
            instance = provider()

        if descriptor.lifetime.is_singleton():
            descriptor.instance = instance

        return instance

    def _create(
        self,
        cls: type,
    ) -> Any:

        signature = inspect.signature(cls.__init__)

        kwargs: dict[str, Any] = {}

        for parameter in list(signature.parameters.values())[1:]:

            annotation = parameter.annotation

            if annotation is inspect.Signature.empty:
                raise DependencyNotRegisteredError(
                    f"{cls.__name__}.{parameter.name} has no type annotation."
                )

            kwargs[parameter.name] = self._container.resolve(annotation)

        return cls(**kwargs)