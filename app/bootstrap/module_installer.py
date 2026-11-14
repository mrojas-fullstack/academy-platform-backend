from __future__ import annotations

import importlib
import importlib.util
import pkgutil

from fastapi import FastAPI

from app.core.container import Container
from app.core.messaging import MessageRegistry
from app.core.scanner import Scanner


class ModuleInstaller:
    def install(
        self,
        package: str,
        app: FastAPI,
        container: Container,
        registry: MessageRegistry,
    ) -> None:
        scanner = Scanner()

        root = importlib.import_module(package)

        for _, module_name, is_package in pkgutil.iter_modules(root.__path__):
            if not is_package:
                continue

            module_package = f"{package}.{module_name}"

            bootstrap_package = f"{module_package}.bootstrap"

            if importlib.util.find_spec(bootstrap_package) is None:
                continue

            bootstrap = importlib.import_module(
                bootstrap_package,
            )

            bootstrap.register_services(
                container,
            )

            bootstrap.register_routes(
                app,
            )

            handlers = scanner.scan(
                module_package,
            )

            for handler in handlers:
                container.register(
                    handler,
                )

                registry.register(
                    handler,
                )
