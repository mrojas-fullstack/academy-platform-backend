from __future__ import annotations

from dataclasses import dataclass

from app.core.messaging.interfaces import Command


@dataclass(slots=True, frozen=True)
class LogoutCommand(Command):
    session_id: str
