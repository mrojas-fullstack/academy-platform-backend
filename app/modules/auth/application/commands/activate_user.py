from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ActivateUserCommand:
    user_id: str
