from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class AuthenticationResult:
    user_id: UUID
    access_token: str
    refresh_token: str
