from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Dormitory(Base):
    __tablename__ = "dormitories"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    address: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    img: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
