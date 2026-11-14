from __future__ import annotations

from datetime import UTC, datetime

from app.core.domain.entities.entity import Entity
from app.modules.auth.domain.enums import TokenStatus
from app.modules.auth.domain.value_objects import (
    RefreshTokenHash,
    RefreshTokenId,
    SessionId,
)


class RefreshToken(Entity[RefreshTokenId]):
    def __init__(
        self,
        refresh_token_id: RefreshTokenId,
        session_id: SessionId,
        token_hash: RefreshTokenHash,
        status: TokenStatus,
        created_at: datetime,
        expires_at: datetime,
    ) -> None:
        super().__init__(refresh_token_id)

        self._session_id = session_id
        self._token_hash = token_hash
        self._status = status
        self._created_at = created_at
        self._expires_at = expires_at

    @property
    def session_id(self) -> SessionId:
        return self._session_id

    @property
    def token_hash(self) -> RefreshTokenHash:
        return self._token_hash

    @property
    def status(self) -> TokenStatus:
        return self._status

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def expires_at(self) -> datetime:
        return self._expires_at

    @property
    def is_active(self) -> bool:
        return self._status is TokenStatus.ACTIVE and self._expires_at > datetime.now(UTC)

    def revoke(self) -> None:
        self._status = TokenStatus.REVOKED

    def expire(self) -> None:
        self._status = TokenStatus.EXPIRED

    def rotate(self) -> None:
        self._status = TokenStatus.ROTATED
