from __future__ import annotations

from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database.base import Base


class IdentityModel(Base):
    __tablename__ = "identities"

    __table_args__ = (
        UniqueConstraint(
            "provider",
            "provider_user_id",
            name="uq_identities_provider_user_id",
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True)

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    provider_user_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    provider_email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
    )

    verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
