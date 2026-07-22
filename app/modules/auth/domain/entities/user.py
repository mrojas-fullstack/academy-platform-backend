from __future__ import annotations

from app.modules.auth.domain.enums import UserStatus
from app.modules.auth.domain.value_objects import SessionId
from app.modules.auth.domain.value_objects import (
    Email,
    Locale,
    PersonName,
    ProfileImage,
    TimeZone,
    UserId,
)

from .aggregate_root import AggregateRoot
from .identity import Identity
from .session import Session
from .user_profile import UserProfile


class User(AggregateRoot):

    def __init__(
        self,
        user_id: UserId,
        status: UserStatus,
        profile: UserProfile,
        identities: list[Identity] | None = None,
        sessions: list[Session] | None = None,
    ) -> None:

        super().__init__(user_id)

        self._status = status
        self._profile = profile
        self._identities = identities or []
        self._sessions = sessions or []

    @property
    def status(self) -> UserStatus:

        return self._status

    @property
    def profile(self) -> UserProfile:

        return self._profile

    @property
    def identities(self) -> tuple[Identity, ...]:

        return tuple(self._identities)

    @property
    def sessions(self) -> tuple[Session, ...]:

        return tuple(self._sessions)

    def activate(self) -> None:

        self._status = UserStatus.ACTIVE

    def suspend(self) -> None:

        self._status = UserStatus.SUSPENDED

    def change_email(
        self,
        email: Email,
    ) -> None:

        self._profile.change_email(email)

    def change_name(
        self,
        first_name: PersonName,
        last_name: PersonName,
    ) -> None:

        self._profile.change_name(
            first_name,
            last_name,
        )

    def change_profile_image(
        self,
        profile_image: ProfileImage,
    ) -> None:

        self._profile.change_profile_image(
            profile_image,
        )

    def change_locale(
        self,
        locale: Locale,
    ) -> None:

        self._profile.change_locale(locale)

    def change_time_zone(
        self,
        time_zone: TimeZone,
    ) -> None:

        self._profile.change_time_zone(
            time_zone,
        )

    def link_identity(
        self,
        identity: Identity,
    ) -> None:

        for existing in self._identities:
            if existing.provider == identity.provider:
                return

        self._identities.append(identity)

    def start_session(
        self,
        session: Session,
    ) -> None:

        self._sessions.append(session)

    def revoke_session(
        self,
        session_id: SessionId,
    ) -> None:

        for session in self._sessions:

            if session.id == session_id:

                session.revoke()

                return