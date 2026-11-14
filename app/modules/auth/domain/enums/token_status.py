from enum import StrEnum


class TokenStatus(StrEnum):
    ACTIVE = "active"

    REVOKED = "revoked"

    EXPIRED = "expired"

    ROTATED = "rotated"
