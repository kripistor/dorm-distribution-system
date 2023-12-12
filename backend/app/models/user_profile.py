from datetime import datetime
from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(GUID, ForeignKey("users.id"))
    card_number: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    birth_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    grant_order_number: Mapped[str] = mapped_column(String(length=32), nullable=True)
    transfer_order_number: Mapped[str] = mapped_column(String(length=32), nullable=True)
    transfer_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    birth_place: Mapped[str] = mapped_column(String(length=32), nullable=True)
    address: Mapped[str] = mapped_column(String(length=32), nullable=True)
