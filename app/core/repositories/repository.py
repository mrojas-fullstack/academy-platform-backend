from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.modules.auth.domain.entities import Entity
from app.modules.auth.domain.value_objects import EntityId

TEntity = TypeVar(
    "TEntity",
    bound=Entity,
)

TEntityId = TypeVar(
    "TEntityId",
    bound=EntityId,
)


class Repository(
    ABC,
    Generic[
        TEntity,
        TEntityId,
    ],
):

    @abstractmethod
    async def add(
        self,
        entity: TEntity,
    ) -> None:
        ...

    @abstractmethod
    async def update(
        self,
        entity: TEntity,
    ) -> None:
        ...

    @abstractmethod
    async def delete(
        self,
        entity_id: TEntityId,
    ) -> None:
        ...

    @abstractmethod
    async def get_by_id(
        self,
        entity_id: TEntityId,
    ) -> TEntity | None:
        ...