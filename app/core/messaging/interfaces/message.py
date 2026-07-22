from dataclasses import dataclass, field
from uuid import UUID, uuid4
from abc import ABC


@dataclass(slots=True)
class Message(ABC):

    message_id: UUID = field(
        default_factory=uuid4
    )