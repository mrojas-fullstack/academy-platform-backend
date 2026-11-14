from __future__ import annotations

from app.modules.auth.domain.entities import RefreshToken
from app.modules.auth.domain.enums import TokenStatus
from app.modules.auth.domain.value_objects import (
    RefreshTokenHash,
    RefreshTokenId,
    SessionId,
)
from app.modules.auth.infrastructure.database.models.refresh_token_model import (
    RefreshTokenModel,
)


class RefreshTokenMapper:
    @staticmethod
    def to_model(entity: RefreshToken) -> RefreshTokenModel:
        return RefreshTokenModel(
            id=entity.id.value,
            session_id=entity.session_id.value,
            token_hash=entity.token_hash.value,
            status=entity.status.value,
            created_at=entity.created_at,
            expires_at=entity.expires_at,
        )

    @staticmethod
    def to_domain(model: RefreshTokenModel) -> RefreshToken:
        return RefreshToken(
            refresh_token_id=RefreshTokenId(model.id),
            session_id=SessionId(model.session_id),
            token_hash=RefreshTokenHash(model.token_hash),
            status=TokenStatus(model.status),
            created_at=model.created_at,
            expires_at=model.expires_at,
        )
