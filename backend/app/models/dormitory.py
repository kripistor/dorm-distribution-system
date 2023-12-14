from typing import Optional, List

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Dormitory(Base):
    __tablename__ = "dormitories"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    address: Mapped[str] = mapped_column(String, index=True, nullable=False)
    img: Mapped[str] = mapped_column(String, index=True, nullable=False)
    scheme: Mapped[str] = mapped_column(String, index=True, nullable=False)
    floors: Mapped[Optional[List["Floor"]]] = relationship("Floor", lazy="raise")
    dormitory_photos: Mapped[Optional[List["DormitoryPhoto"]]] = relationship(
        "DormitoryPhoto", lazy="raise"
    )
