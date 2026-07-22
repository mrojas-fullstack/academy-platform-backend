from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.database.DATABASE_URL,
    echo=settings.database.DATABASE_ECHO,
)


SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
)


def get_session() -> Generator[Session, None, None]:
    """
    Database session dependency.
    """

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()