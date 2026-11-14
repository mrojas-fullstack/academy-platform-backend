from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.domain.entities import Identity
from app.modules.auth.domain.enums import IdentityProvider
from app.modules.auth.domain.repositories import IdentityRepository
from app.modules.auth.domain.value_objects import (
    IdentityId,
    ProviderUserId,
    UserId,
)
from app.modules.auth.infrastructure.database.models.identity_model import (
    IdentityModel,
)
from app.modules.auth.infrastructure.mappers.identity_mapper import IdentityMapper


class SQLAlchemyIdentityRepository(IdentityRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, entity: Identity) -> None:
        self._session.add(IdentityMapper.to_model(entity))

    async def update(self, entity: Identity) -> None:
        await self._session.merge(IdentityMapper.to_model(entity))

    async def delete(self, entity_id: IdentityId) -> None:
        model = await self._session.get(IdentityModel, entity_id.value)

        if model is not None:
            await self._session.delete(model)

    async def get_by_id(self, entity_id: IdentityId) -> Identity | None:
        model = await self._session.get(IdentityModel, entity_id.value)

        if model is None:
            return None

        return IdentityMapper.to_domain(model)

    async def get_by_provider(
        self,
        provider: IdentityProvider,
        provider_user_id: ProviderUserId,
    ) -> Identity | None:
        statement = select(IdentityModel).where(
            IdentityModel.provider == provider.value,
            IdentityModel.provider_user_id == provider_user_id.value,
        )

        model = await self._session.scalar(statement)

        if model is None:
            return None

        return IdentityMapper.to_domain(model)

    async def get_by_user_id(self, user_id: UserId) -> list[Identity]:
        statement = select(IdentityModel).where(
            IdentityModel.user_id == user_id.value,
        )

        models = await self._session.scalars(statement)

        return [IdentityMapper.to_domain(model) for model in models.all()]

    async def exists(
        self,
        provider: IdentityProvider,
        provider_user_id: ProviderUserId,
    ) -> bool:
        statement = select(IdentityModel.id).where(
            IdentityModel.provider == provider.value,
            IdentityModel.provider_user_id == provider_user_id.value,
        )

        result = await self._session.scalar(statement)

        return result is not None
