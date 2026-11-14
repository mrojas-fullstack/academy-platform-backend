from __future__ import annotations

from dataclasses import dataclass

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import (
    IdentityId,
    UserId,
)


@dataclass(slots=True)
class IdentityLinkedEvent(DomainEvent):
    user_id: UserId

    identity_id: IdentityId
