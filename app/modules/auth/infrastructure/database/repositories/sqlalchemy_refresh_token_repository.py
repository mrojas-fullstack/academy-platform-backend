from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.domain.entities import RefreshToken
from app.modules.auth.domain.repositories import RefreshTokenRepository
from app.modules.auth.domain.value_objects import (
    RefreshTokenHash,
    RefreshTokenId,
    SessionId,
)
from app.modules.auth.infrastructure.database.models.refresh_token_model import (
    RefreshTokenModel,
)
from app.modules.auth.infrastructure.mappers.refresh_token_mapper import (
    RefreshTokenMapper,
)


class SQLAlchemyRefreshTokenRepository(RefreshTokenRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, entity: RefreshToken) -> None:
        self._session.add(RefreshTokenMapper.to_model(entity))

    async def update(self, entity: RefreshToken) -> None:
        await self._session.merge(RefreshTokenMapper.to_model(entity))

    async def delete(self, entity_id: RefreshTokenId) -> None:
        model = await self._session.get(
            RefreshTokenModel,
            entity_id.value,
        )

        if model is not None:
            await self._session.delete(model)

    async def get_by_id(
        self,
        entity_id: RefreshTokenId,
    ) -> RefreshToken | None:
        model = await self._session.get(
            RefreshTokenModel,
            entity_id.value,
        )

        if model is None:
            return None

        return RefreshTokenMapper.to_domain(model)

    async def get_by_session_id(
        self,
        session_id: SessionId,
    ) -> list[RefreshToken]:
        statement = select(RefreshTokenModel).where(
            RefreshTokenModel.session_id == session_id.value,
        )

        models = await self._session.scalars(statement)

        return [RefreshTokenMapper.to_domain(model) for model in models.all()]

    async def get_by_hash(
        self,
        token_hash: RefreshTokenHash,
    ) -> RefreshToken | None:
        statement = (
            select(RefreshTokenModel)
            .where(
                RefreshTokenModel.token_hash == token_hash.value,
            )
            .with_for_update()
        )

        model = await self._session.scalar(statement)

        if model is None:
            return None

        return RefreshTokenMapper.to_domain(model)
