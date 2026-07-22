from __future__ import annotations

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import (
    RefreshTokenId,
    SessionId,
)


class RefreshTokenRotatedEvent(DomainEvent):

    def __init__(
        self,
        refresh_token_id: RefreshTokenId,
        session_id: SessionId,
    ) -> None:

        super().__init__()

        self._refresh_token_id = refresh_token_id
        self._session_id = session_id

    @property
    def refresh_token_id(self) -> RefreshTokenId:

        return self._refresh_token_id

    @property
    def session_id(self) -> SessionId:

        return self._session_id