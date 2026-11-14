from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.domain.entities import User
from app.modules.auth.domain.repositories import UserRepository
from app.modules.auth.domain.value_objects import Email, UserId
from app.modules.auth.infrastructure.database.models.user_model import UserModel
from app.modules.auth.infrastructure.database.models.user_profile_model import (
    UserProfileModel,
)
from app.modules.auth.infrastructure.mappers.user_mapper import UserMapper


class SQLAlchemyUserRepository(UserRepository):
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self._session = session

    async def add(
        self,
        entity: User,
    ) -> None:
        model = UserMapper.to_model(entity)

        self._session.add(model)

        await self._session.flush()

    async def update(
        self,
        entity: User,
    ) -> None:
        model = UserMapper.to_model(entity)

        await self._session.merge(model)

    async def delete(
        self,
        entity_id: UserId,
    ) -> None:
        model = await self._session.get(
            UserModel,
            entity_id.value,
        )

        if model is not None:
            await self._session.delete(model)

    async def get_by_id(
        self,
        entity_id: UserId,
    ) -> User | None:
        model = await self._session.get(
            UserModel,
            entity_id.value,
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)

    async def get_by_email(
        self,
        email: Email,
    ) -> User | None:
        statement = (
            select(UserModel)
            .join(UserProfileModel)
            .where(
                UserProfileModel.email == email.value,
            )
        )

        model = await self._session.scalar(statement)

        if model is None:
            return None

        return UserMapper.to_domain(model)

    async def exists_by_email(
        self,
        email: Email,
    ) -> bool:
        statement = (
            select(UserModel.id)
            .join(UserProfileModel)
            .where(
                UserProfileModel.email == email.value,
            )
        )

        result = await self._session.scalar(statement)

        return result is not None
