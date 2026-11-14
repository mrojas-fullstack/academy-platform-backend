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
from app.modules.auth.infrastructure.database.models.user_model import UserModel
from app.modules.auth.infrastructure.database.models.user_profile_model import (
    UserProfileModel,
)


class UserMapper:
    @staticmethod
    def to_model(
        user: User,
    ) -> UserModel:

        model = UserModel(
            id=user.id.value,
            status=user.status.value,
        )

        model.profile = UserProfileModel(
            user_id=user.id.value,
            email=user.profile.email.value,
            first_name=user.profile.first_name.value,
            last_name=user.profile.last_name.value,
            profile_image=(
                user.profile.profile_image.value if user.profile.profile_image is not None else None
            ),
            locale=user.profile.locale.value,
            time_zone=user.profile.time_zone.value,
        )

        return model

    @staticmethod
    def to_domain(
        model: UserModel,
    ) -> User:

        if model.profile is None:
            raise RuntimeError(f"User {model.id} does not have a profile.")

        profile = UserProfile(
            profile_id=UserProfileId(model.id),
            email=Email(model.profile.email),
            first_name=PersonName(model.profile.first_name),
            last_name=PersonName(model.profile.last_name),
            profile_image=(
                ProfileImage(
                    model.profile.profile_image,
                )
                if model.profile.profile_image is not None
                else None
            ),
            locale=Locale(model.profile.locale),
            time_zone=TimeZone(model.profile.time_zone),
        )

        return User(
            user_id=UserId(model.id),
            status=UserStatus(model.status),
            profile=profile,
        )
