from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.domain.entities import Session
from app.modules.auth.domain.enums import SessionStatus
from app.modules.auth.domain.repositories import SessionRepository
from app.modules.auth.domain.value_objects import SessionId, UserId
from app.modules.auth.infrastructure.database.models.session_model import (
    SessionModel,
)
from app.modules.auth.infrastructure.mappers.session_mapper import SessionMapper


class SQLAlchemySessionRepository(SessionRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, entity: Session) -> None:
        self._session.add(SessionMapper.to_model(entity))
        await self._session.flush()

    async def update(self, entity: Session) -> None:
        await self._session.merge(SessionMapper.to_model(entity))

    async def delete(self, entity_id: SessionId) -> None:
        model = await self._session.get(SessionModel, entity_id.value)

        if model is not None:
            await self._session.delete(model)

    async def get_by_id(self, entity_id: SessionId) -> Session | None:
        model = await self._session.get(SessionModel, entity_id.value)

        if model is None:
            return None

        return SessionMapper.to_domain(model)

    async def get_active_by_user_id(self, user_id: UserId) -> list[Session]:
        statement = select(SessionModel).where(
            SessionModel.user_id == user_id.value,
            SessionModel.status == SessionStatus.ACTIVE.value,
        )

        models = await self._session.scalars(statement)

        return [SessionMapper.to_domain(model) for model in models.all()]
