from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base

if TYPE_CHECKING:
    from app.models.item import Item  # noqa: F401

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    login: Mapped[str] = mapped_column(String, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)


    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"

