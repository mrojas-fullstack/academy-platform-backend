from __future__ import annotations

from abc import abstractmethod

from app.core.repositories.repository import Repository
from app.modules.auth.domain.entities import RefreshToken
from app.modules.auth.domain.value_objects import RefreshTokenId, SessionId
from app.modules.auth.domain.value_objects.refresh_token_hash import RefreshTokenHash


class RefreshTokenRepository(
    Repository[RefreshToken, RefreshTokenId],
):
    @abstractmethod
    async def get_by_session_id(
        self,
        session_id: SessionId,
    ) -> list[RefreshToken]: ...

    @abstractmethod
    async def get_by_hash(
        self,
        token_hash: RefreshTokenHash,
    ) -> RefreshToken | None: ...
