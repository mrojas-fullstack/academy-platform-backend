from dataclasses import dataclass, field
from datetime import UTC, datetime

from .message import Message


@dataclass(
    slots=True,
    frozen=True,
)
class Event(Message):
    occurred_on: datetime = field(default_factory=lambda: datetime.now(UTC))
