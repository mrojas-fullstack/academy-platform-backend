from __future__ import annotations

from pydantic import BaseModel


class RegisterResponse(BaseModel):
    id: str

    message: str
