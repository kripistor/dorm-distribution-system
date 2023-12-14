from typing import Optional, List

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class DormitoryPhoto(Base):
    __tablename__ = "dormitory_photos"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    dormitory_id: Mapped[int] = mapped_column(Integer, ForeignKey("dormitories.id"))
    img: Mapped[str] = mapped_column(String(length=32), index=True, nullable=False)
