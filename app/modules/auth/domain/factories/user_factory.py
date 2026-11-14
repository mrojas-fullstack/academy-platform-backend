from __future__ import annotations

from app.modules.auth.domain.entities import User, UserProfile
from app.modules.auth.domain.enums import UserStatus
from app.modules.auth.domain.value_objects import (
    Email,
    Locale,
    PersonName,
    ProfileImage,
    TimeZone,
    UserId,
    UserProfileId,
)


class UserFactory:
    @staticmethod
    def register(
        email: Email,
        first_name: PersonName,
        last_name: PersonName,
        locale: Locale,
        time_zone: TimeZone,
        profile_image: ProfileImage | None = None,
    ) -> User:

        user_id = UserId.new()

        profile = UserProfile(
            profile_id=UserProfileId(user_id.value),
            email=email,
            first_name=first_name,
            last_name=last_name,
            locale=locale,
            time_zone=time_zone,
            profile_image=profile_image,
        )

        return User(
            user_id=user_id,
            status=UserStatus.ACTIVE,
            profile=profile,
        )
