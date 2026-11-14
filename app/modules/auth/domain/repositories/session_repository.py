from __future__ import annotations

from abc import abstractmethod

from app.core.repositories.repository import Repository
from app.modules.auth.domain.entities import Session
from app.modules.auth.domain.value_objects import SessionId, UserId


class SessionRepository(Repository[Session, SessionId]):
    @abstractmethod
    async def get_active_by_user_id(
        self,
        user_id: UserId,
    ) -> list[Session]: ...
