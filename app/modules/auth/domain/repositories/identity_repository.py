from __future__ import annotations

from abc import abstractmethod

from app.core.repositories.repository import Repository
from app.modules.auth.domain.entities import Identity
from app.modules.auth.domain.enums import IdentityProvider
from app.modules.auth.domain.value_objects import (
    IdentityId,
    ProviderUserId,
    UserId,
)


class IdentityRepository(Repository[Identity, IdentityId]):
    @abstractmethod
    async def get_by_provider(
        self,
        provider: IdentityProvider,
        provider_user_id: ProviderUserId,
    ) -> Identity | None: ...

    @abstractmethod
    async def get_by_user_id(
        self,
        user_id: UserId,
    ) -> list[Identity]: ...

    @abstractmethod
    async def exists(
        self,
        provider: IdentityProvider,
        provider_user_id: ProviderUserId,
    ) -> bool: ...
