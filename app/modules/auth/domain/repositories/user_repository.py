from __future__ import annotations

from abc import abstractmethod

from app.core.repositories import Repository
from app.modules.auth.domain.entities import User
from app.modules.auth.domain.value_objects import (
    Email,
    UserId,
)


class UserRepository(
    Repository[
        User,
        UserId,
    ],
):
    @abstractmethod
    async def get_by_email(
        self,
        email: Email,
    ) -> User | None: ...

    @abstractmethod
    async def exists_by_email(
        self,
        email: Email,
    ) -> bool: ...
