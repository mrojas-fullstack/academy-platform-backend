from __future__ import annotations

from datetime import UTC, datetime

from app.core.domain.entities.entity import Entity
from app.modules.auth.domain.enums import SessionStatus
from app.modules.auth.domain.value_objects import (
    SessionId,
    UserId,
)


class Session(Entity[SessionId]):
    def __init__(
        self,
        session_id: SessionId,
        user_id: UserId,
        status: SessionStatus,
        created_at: datetime,
        expires_at: datetime,
        last_activity_at: datetime,
    ) -> None:

        super().__init__(session_id)

        self._user_id = user_id
        self._status = status
        self._created_at = created_at
        self._expires_at = expires_at
        self._last_activity_at = last_activity_at

    @property
    def user_id(self) -> UserId:

        return self._user_id

    @property
    def status(self) -> SessionStatus:

        return self._status

    @property
    def created_at(self) -> datetime:

        return self._created_at

    @property
    def expires_at(self) -> datetime:

        return self._expires_at

    @property
    def last_activity_at(self) -> datetime:

        return self._last_activity_at

    @property
    def is_active(self) -> bool:

        return self._status is SessionStatus.ACTIVE and self._expires_at > datetime.now(UTC)

    def touch(
        self,
        at: datetime,
    ) -> None:

        self._last_activity_at = at

    def revoke(self) -> None:

        self._status = SessionStatus.REVOKED

    def expire(self) -> None:

        self._status = SessionStatus.EXPIRED
