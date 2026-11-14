from __future__ import annotations

from app.core.domain.entities import Entity
from app.modules.auth.domain.value_objects import (
    Email,
    Locale,
    PersonName,
    ProfileImage,
    TimeZone,
    UserProfileId,
)


class UserProfile(Entity[UserProfileId]):
    def __init__(
        self,
        profile_id: UserProfileId,
        email: Email,
        first_name: PersonName,
        last_name: PersonName,
        profile_image: ProfileImage | None,
        locale: Locale,
        time_zone: TimeZone,
    ) -> None:

        super().__init__(profile_id)

        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._profile_image = profile_image
        self._locale = locale
        self._time_zone = time_zone

    @property
    def email(self) -> Email:

        return self._email

    @property
    def first_name(self) -> PersonName:

        return self._first_name

    @property
    def last_name(self) -> PersonName:

        return self._last_name

    @property
    def profile_image(self) -> ProfileImage | None:

        return self._profile_image

    @property
    def locale(self) -> Locale:

        return self._locale

    @property
    def time_zone(self) -> TimeZone:

        return self._time_zone

    def change_email(
        self,
        email: Email,
    ) -> None:

        self._email = email

    def change_name(
        self,
        first_name: PersonName,
        last_name: PersonName,
    ) -> None:

        self._first_name = first_name
        self._last_name = last_name

    def change_profile_image(
        self,
        profile_image: ProfileImage | None,
    ) -> None:

        self._profile_image = profile_image

    def change_locale(
        self,
        locale: Locale,
    ) -> None:

        self._locale = locale

    def change_time_zone(
        self,
        time_zone: TimeZone,
    ) -> None:

        self._time_zone = time_zone
