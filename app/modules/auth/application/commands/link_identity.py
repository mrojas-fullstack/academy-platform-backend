from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class LinkIdentityCommand:

    user_id: str

    provider: str

    authorization_code: str