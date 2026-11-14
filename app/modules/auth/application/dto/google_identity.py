from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GoogleIdentity:
    provider_user_id: str
    email: str
    first_name: str
    last_name: str
    profile_image: str | None
    email_verified: bool
