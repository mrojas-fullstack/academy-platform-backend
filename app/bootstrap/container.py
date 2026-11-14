from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.database import (
    SQLAlchemyUnitOfWork,
    UnitOfWork,
)
from app.core.database.session import (
    configure_database,
    get_session_factory,
)
from app.core.logging import logger
from app.core.settings import Settings


def build_container(
    settings: Settings,
) -> Container:

    configure_database(settings)

    container = Container()

    container.register_instance(
        Settings,
        settings,
    )

    container.register_instance(
        type(logger),
        logger,
    )

    container.register_factory(
        AsyncSession,
        lambda: get_session_factory(),
    )

    container.register_factory(
        UnitOfWork,
        lambda: SQLAlchemyUnitOfWork(
            container.resolve(AsyncSession),
        ),
    )

    return container
