from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class LoginCommand:

    provider: str

    authorization_code: str