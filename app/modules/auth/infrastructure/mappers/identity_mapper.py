from __future__ import annotations

from app.modules.auth.domain.entities import Identity
from app.modules.auth.domain.enums import IdentityProvider
from app.modules.auth.domain.value_objects import (
    Email,
    IdentityId,
    ProviderUserId,
    UserId,
)
from app.modules.auth.infrastructure.database.models.identity_model import (
    IdentityModel,
)


class IdentityMapper:
    @staticmethod
    def to_model(entity: Identity) -> IdentityModel:
        return IdentityModel(
            id=entity.id.value,
            user_id=entity.user_id.value,
            provider=entity.provider.value,
            provider_user_id=entity.provider_user_id.value,
            provider_email=entity.provider_email.value,
            verified=entity.verified,
        )

    @staticmethod
    def to_domain(model: IdentityModel) -> Identity:
        return Identity(
            identity_id=IdentityId(model.id),
            user_id=UserId(model.user_id),
            provider=IdentityProvider(model.provider),
            provider_user_id=ProviderUserId(model.provider_user_id),
            provider_email=Email(model.provider_email),
            verified=model.verified,
        )
