from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(
    slots=True,
    frozen=True,
    kw_only=True,
)
class Message:
    message_id: UUID = field(
        default_factory=uuid4,
    )
