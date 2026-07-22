from __future__ import annotations

from app.modules.auth.domain.enums import IdentityProvider
from app.modules.auth.domain.value_objects import (
    Email,
    IdentityId,
    ProviderUserId,
    UserId,
)

from .entity import Entity


class Identity(Entity):

    def __init__(
        self,
        identity_id: IdentityId,
        user_id: UserId,
        provider: IdentityProvider,
        provider_user_id: ProviderUserId,
        provider_email: Email,
        verified: bool,
    ) -> None:

        super().__init__(identity_id)

        self._user_id = user_id
        self._provider = provider
        self._provider_user_id = provider_user_id
        self._provider_email = provider_email
        self._verified = verified

    @property
    def user_id(self) -> UserId:

        return self._user_id

    @property
    def provider(self) -> IdentityProvider:

        return self._provider

    @property
    def provider_user_id(self) -> ProviderUserId:

        return self._provider_user_id

    @property
    def provider_email(self) -> Email:

        return self._provider_email

    @property
    def verified(self) -> bool:

        return self._verified

    def verify(self) -> None:

        self._verified = True