from app.core.container import Container, ServiceLifetime
from app.core.logging import logger
from app.core.settings import Settings


def build_container(
    settings: Settings,
) -> Container:

    container = Container()

    container.register_instance(
        Settings,
        settings,
    )

    container.register_instance(
        type(logger),
        logger,
    )

    return container