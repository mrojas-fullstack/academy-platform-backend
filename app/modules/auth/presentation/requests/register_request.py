from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    email: EmailStr

    first_name: str = Field(
        min_length=2,
        max_length=100,
    )

    last_name: str = Field(
        min_length=2,
        max_length=100,
    )

    locale: str

    time_zone: str

    profile_image: str | None = None
