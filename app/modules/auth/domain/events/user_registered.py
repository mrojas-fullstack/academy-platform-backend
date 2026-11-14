from __future__ import annotations

from dataclasses import dataclass

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import UserId


@dataclass(slots=True)
class UserRegisteredEvent(DomainEvent):
    user_id: UserId
