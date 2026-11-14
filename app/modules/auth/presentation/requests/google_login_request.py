from __future__ import annotations

from pydantic import BaseModel, Field


class GoogleLoginRequest(BaseModel):
    credential: str = Field(min_length=1)
    locale: str = Field(min_length=2, max_length=20)
    time_zone: str = Field(min_length=1, max_length=100)
