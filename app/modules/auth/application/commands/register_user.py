from __future__ import annotations

from dataclasses import dataclass

from app.core.messaging.interfaces import Command


@dataclass(slots=True, frozen=True)
class RegisterUserCommand(Command):
    email: str

    first_name: str

    last_name: str

    locale: str

    time_zone: str

    profile_image: str | None
