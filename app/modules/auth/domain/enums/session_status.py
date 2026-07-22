from enum import StrEnum


class SessionStatus(StrEnum):

    ACTIVE = "active"

    EXPIRED = "expired"

    REVOKED = "revoked"