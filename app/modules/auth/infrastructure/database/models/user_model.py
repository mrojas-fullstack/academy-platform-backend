from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base import Base

if TYPE_CHECKING:
    from .user_profile_model import UserProfileModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    profile: Mapped[UserProfileModel] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined",
    )
