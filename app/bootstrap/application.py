from fastapi import FastAPI

from app.core.database import configure_database
from app.core.settings import get_settings

from .container import build_container
from .context import ApplicationContext
from .messaging import build_messaging
from .module_installer import ModuleInstaller


class ApplicationBootstrap:
    def build(
        self,
        app: FastAPI,
    ) -> ApplicationContext:

        settings = get_settings()

        configure_database(
            settings,
        )

        container = build_container(
            settings,
        )

        registry, bus = build_messaging(
            container,
        )

        installer = ModuleInstaller()

        installer.install(
            package="app.modules",
            app=app,
            container=container,
            registry=registry,
        )

        return ApplicationContext(
            settings=settings,
            container=container,
            registry=registry,
            bus=bus,
        )
