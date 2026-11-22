from __future__ import annotations

from abc import abstractmethod

from app.core.repositories import Repository
from app.modules.auth.domain.entities import LocalCredential
from app.modules.auth.domain.value_objects import (
    LoginIdentifier,
    UserId,
)


class LocalCredentialRepository(
    Repository[LocalCredential, UserId],
):
    @abstractmethod
    async def get_by_identifier(
        self,
        identifier: LoginIdentifier,
    ) -> LocalCredential | None: ...

    @abstractmethod
    async def exists_by_identifier(
        self,
        identifier: LoginIdentifier,
    ) -> bool: ...
