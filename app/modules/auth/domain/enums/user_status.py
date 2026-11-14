from enum import StrEnum


class UserStatus(StrEnum):
    PENDING = "pending"

    ACTIVE = "active"

    SUSPENDED = "suspended"

    DELETED = "deleted"
