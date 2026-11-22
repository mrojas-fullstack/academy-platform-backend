from __future__ import annotations

from pydantic import BaseModel


class MeResponse(BaseModel):
    id: str
    email: str | None
    first_name: str
    last_name: str
    profile_image: str | None
    locale: str
    time_zone: str
