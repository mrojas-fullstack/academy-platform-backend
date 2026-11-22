from app.core.container import Container
from app.core.logging import logger
from app.core.security import PasswordHasher
from app.core.settings import Settings
from app.modules.auth.infrastructure.security import Argon2PasswordHasher


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

    container.register_instance(
        PasswordHasher,
        Argon2PasswordHasher(),
    )

    return container
