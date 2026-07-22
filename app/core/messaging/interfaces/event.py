from datetime import UTC, datetime
from dataclasses import dataclass, field

from .message import Message


@dataclass(slots=True)
class Event(Message):

    occurred_on: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )