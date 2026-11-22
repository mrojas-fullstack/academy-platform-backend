from __future__ import annotations

from app.core.domain.entities.entity import Entity
from app.modules.auth.domain.value_objects import (
    LoginIdentifier,
    PasswordHash,
    UserId,
)


class LocalCredential(Entity[UserId]):
    def __init__(
        self,
        user_id: UserId,
        identifier: LoginIdentifier,
        password_hash: PasswordHash,
    ) -> None:
        super().__init__(user_id)

        self._identifier = identifier
        self._password_hash = password_hash

    @property
    def user_id(self) -> UserId:
        return self.id

    @property
    def identifier(self) -> LoginIdentifier:
        return self._identifier

    @property
    def password_hash(self) -> PasswordHash:
        return self._password_hash

    def change_identifier(
        self,
        identifier: LoginIdentifier,
    ) -> None:
        self._identifier = identifier

    def change_password(
        self,
        password_hash: PasswordHash,
    ) -> None:
        self._password_hash = password_hash
