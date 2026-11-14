from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base import Base

if TYPE_CHECKING:
    from .user_model import UserModel


class UserProfileModel(Base):
    __tablename__ = "user_profiles"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        index=True,
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    profile_image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    locale: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    time_zone: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    user: Mapped[UserModel] = relationship(
        back_populates="profile",
    )
