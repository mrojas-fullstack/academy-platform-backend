from __future__ import annotations

import re

from app.core.domain.value_objects.value_object import ValueObject

from ..exceptions import InvalidLoginIdentifierException
from .email import Email
from .login_identifier_type import LoginIdentifierType

_USERNAME_REGEX = re.compile(r"^[a-z0-9._-]{3,30}$")


class LoginIdentifier(ValueObject):
    def __init__(
        self,
        value: str,
        identifier_type: LoginIdentifierType,
    ) -> None:
        if identifier_type == LoginIdentifierType.EMAIL:
            self._value = Email(value).value

        elif identifier_type == LoginIdentifierType.USERNAME:
            normalized_value = value.strip().lower()

            if not _USERNAME_REGEX.fullmatch(normalized_value):
                raise InvalidLoginIdentifierException(value)

            self._value = normalized_value

        else:
            raise ValueError("Unsupported login identifier type.")

        self._type = identifier_type

    @property
    def value(self) -> str:
        return self._value

    @property
    def type(self) -> LoginIdentifierType:
        return self._type

    def __str__(self) -> str:
        return self._value
