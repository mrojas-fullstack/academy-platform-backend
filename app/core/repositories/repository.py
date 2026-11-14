from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from app.core.domain.entities import Entity
from app.core.domain.value_objects import EntityId


class Repository[
    TEntity: Entity[Any],
    TEntityId: EntityId,
](ABC):
    @abstractmethod
    async def add(
        self,
        entity: TEntity,
    ) -> None: ...

    @abstractmethod
    async def update(
        self,
        entity: TEntity,
    ) -> None: ...

    @abstractmethod
    async def delete(
        self,
        entity_id: TEntityId,
    ) -> None: ...

    @abstractmethod
    async def get_by_id(
        self,
        entity_id: TEntityId,
    ) -> TEntity | None: ...
