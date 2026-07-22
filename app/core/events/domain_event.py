from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(slots=True, kw_only=True)
class DomainEvent(ABC):

    event_id: UUID = field(default_factory=uuid4)

    occurred_on: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )