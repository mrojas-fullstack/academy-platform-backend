from __future__ import annotations

from app.core.database import UnitOfWork
from app.core.messaging.interfaces import CommandHandler
from app.modules.auth.application.commands import RegisterUserCommand
from app.modules.auth.domain.exceptions import (
    EmailAlreadyExistsException,
)
from app.modules.auth.domain.factories import UserFactory
from app.modules.auth.domain.repositories import UserRepository
from app.modules.auth.domain.value_objects import (
    Email,
    Locale,
    PersonName,
    ProfileImage,
    TimeZone,
    UserId,
)


class RegisterUserHandler(
    CommandHandler[
        RegisterUserCommand,
        UserId,
    ],
):
    def __init__(
        self,
        user_repository: UserRepository,
        unit_of_work: UnitOfWork,
    ) -> None:

        self._user_repository = user_repository
        self._unit_of_work = unit_of_work

    async def handle(
        self,
        command: RegisterUserCommand,
    ) -> UserId:

        email = Email(command.email)

        if await self._user_repository.exists_by_email(email):
            raise EmailAlreadyExistsException(email.value)

        first_name = PersonName(command.first_name)

        last_name = PersonName(command.last_name)

        locale = Locale(command.locale)

        time_zone = TimeZone(command.time_zone)

        profile_image = ProfileImage(command.profile_image) if command.profile_image else None

        user = UserFactory.register(
            email=email,
            first_name=first_name,
            last_name=last_name,
            locale=locale,
            time_zone=time_zone,
            profile_image=profile_image,
        )

        await self._user_repository.add(user)

        await self._unit_of_work.commit()

        return user.id
