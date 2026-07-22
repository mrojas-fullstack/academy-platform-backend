from __future__ import annotations

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import (
    SessionId,
    UserId,
)


class SessionRevokedEvent(DomainEvent):

    def __init__(
        self,
        user_id: UserId,
        session_id: SessionId,
    ) -> None:

        super().__init__()

        self._user_id = user_id
        self._session_id = session_id

    @property
    def user_id(self) -> UserId:

        return self._user_id

    @property
    def session_id(self) -> SessionId:

        return self._session_id