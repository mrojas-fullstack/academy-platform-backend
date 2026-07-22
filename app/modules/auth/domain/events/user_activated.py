from __future__ import annotations

from app.core.events import DomainEvent
from app.modules.auth.domain.value_objects import UserId


class UserActivatedEvent(DomainEvent):

    def __init__(
        self,
        user_id: UserId,
    ) -> None:

        super().__init__()

        self._user_id = user_id

    @property
    def user_id(self) -> UserId:

        return self._user_id