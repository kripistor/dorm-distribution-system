from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Floor(Base):
    __tablename__ = "floors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    dormitory_id: Mapped[int] = mapped_column(Integer, ForeignKey("dormitories.id"))
