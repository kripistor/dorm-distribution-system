from datetime import datetime
from uuid import UUID

from sqlalchemy import String, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    card_number: Mapped[str] = mapped_column(String, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    birth_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    grant_order_number: Mapped[str] = mapped_column(String, nullable=True)
    transfer_order_number: Mapped[str] = mapped_column(String, nullable=True)
    transfer_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    birth_place: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    concession: Mapped[bool] = mapped_column(Boolean, default=False)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    course: Mapped[int] = mapped_column(Integer, nullable=True)

    room_distribution: Mapped["PersonAttachedRoom"] = relationship(
        "PersonAttachedRoom",
        lazy="joined",
        primaryjoin="PersonAttachedRoom.user_id == UserProfile.user_id",
        foreign_keys="PersonAttachedRoom.user_id",
    )
