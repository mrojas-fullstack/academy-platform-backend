from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RegisterUserCommand:

    email: str

    first_name: str

    last_name: str

    locale: str

    time_zone: str

    profile_image: str | None