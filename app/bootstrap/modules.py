import pkgutil

from app.core.container import Container
from app.core.messaging import MessageRegistry
from app.core.scanner import Scanner


def register_modules(
    package: str,
    container: Container,
    registry: MessageRegistry,
) -> None:

    scanner = Scanner()

    root = __import__(
        package,
        fromlist=[""],
    )

    for _, module_name, is_package in pkgutil.iter_modules(root.__path__):

        if not is_package:
            continue

        handlers = scanner.scan(
            f"{package}.{module_name}",
        )

        for handler in handlers:

            container.register(handler)

            registry.register(handler)