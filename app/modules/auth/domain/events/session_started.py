from __future__ import annotations

from dataclasses import dataclass

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import (
    SessionId,
    UserId,
)


@dataclass(slots=True)
class SessionStartedEvent(DomainEvent):
    user_id: UserId

    session_id: SessionId
