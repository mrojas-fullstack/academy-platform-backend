from __future__ import annotations

from pydantic import BaseModel


class GoogleLoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
