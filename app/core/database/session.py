from __future__ import annotations

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.settings import Settings

_engine: AsyncEngine | None = None

_session_factory: async_sessionmaker[AsyncSession] | None = None


def configure_database(
    settings: Settings,
) -> None:
    global _engine
    global _session_factory

    _engine = create_async_engine(
        settings.database.DATABASE_URL,
        echo=settings.database.DATABASE_ECHO,
    )

    _session_factory = async_sessionmaker(
        bind=_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


def get_engine() -> AsyncEngine:
    if _engine is None:
        raise RuntimeError("Database has not been configured.")

    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    if _session_factory is None:
        raise RuntimeError("Database has not been configured.")

    return _session_factory


async def get_session() -> AsyncGenerator[AsyncSession]:
    session_factory = get_session_factory()

    async with session_factory() as session:
        try:
            yield session

        except Exception:
            await session.rollback()
            raise
