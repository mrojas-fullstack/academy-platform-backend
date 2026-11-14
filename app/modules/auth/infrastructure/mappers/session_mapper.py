from __future__ import annotations

from app.modules.auth.domain.entities import Session
from app.modules.auth.domain.enums import SessionStatus
from app.modules.auth.domain.value_objects import SessionId, UserId
from app.modules.auth.infrastructure.database.models.session_model import (
    SessionModel,
)


class SessionMapper:
    @staticmethod
    def to_model(entity: Session) -> SessionModel:
        return SessionModel(
            id=entity.id.value,
            user_id=entity.user_id.value,
            status=entity.status.value,
            created_at=entity.created_at,
            expires_at=entity.expires_at,
            last_activity_at=entity.last_activity_at,
        )

    @staticmethod
    def to_domain(model: SessionModel) -> Session:
        return Session(
            session_id=SessionId(model.id),
            user_id=UserId(model.user_id),
            status=SessionStatus(model.status),
            created_at=model.created_at,
            expires_at=model.expires_at,
            last_activity_at=model.last_activity_at,
        )
