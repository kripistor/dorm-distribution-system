from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Shedule(Base):
    __tablename__ = "schedules"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    institute_name: Mapped[str] = mapped_column(
        String(length=32), index=True, nullable=False
    )
    interval: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
    color: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
