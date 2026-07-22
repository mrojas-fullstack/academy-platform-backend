from app.core.settings import get_settings

from .container import build_container
from .context import ApplicationContext
from .messaging import build_messaging
from .modules import register_modules


class ApplicationBootstrap:

    def build(self) -> ApplicationContext:

        settings = get_settings()

        container = build_container(
            settings,
        )

        registry, bus = build_messaging(
            container,
        )

        register_modules(
            package="app.modules",
            container=container,
            registry=registry,
        )

        return ApplicationContext(
            settings=settings,
            container=container,
            registry=registry,
            bus=bus,
        )