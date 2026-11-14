from __future__ import annotations

from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domain.entities import Entity
from app.core.domain.value_objects.entity_id import EntityId
from app.core.repositories import Repository


class SQLAlchemyRepository[
    TEntity: Entity[EntityId],
    TId: EntityId,
    TModel,
](
    Repository[TEntity, TId],
    ABC,
):
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:

        self._session = session

    @property
    def session(
        self,
    ) -> AsyncSession:

        return self._session

    @property
    @abstractmethod
    def model(
        self,
    ) -> type[TModel]: ...
