from __future__ import annotations

from dataclasses import dataclass

from app.core.messaging.interfaces import Command


@dataclass(frozen=True, slots=True)
class GoogleLoginCommand(Command):
    credential: str
    locale: str
    time_zone: str
