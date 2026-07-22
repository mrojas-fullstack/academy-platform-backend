from __future__ import annotations

from abc import abstractmethod

from app.core.repositories import Repository

from app.modules.auth.domain.entities import RefreshToken
from app.modules.auth.domain.value_objects import (
    RefreshTokenId,
    SessionId,
)


class RefreshTokenRepository(
    Repository[
        RefreshToken,
        RefreshTokenId,
    ],
):

    @abstractmethod
    async def get_by_session_id(
        self,
        session_id: SessionId,
    ) -> list[RefreshToken]:
        ...