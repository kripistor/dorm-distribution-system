from typing import Optional, List

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base
from app.schemas.floor import FloorRead


class Floor(Base):
    __tablename__ = "floors"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    dormitory_id: Mapped[int] = mapped_column(Integer, ForeignKey("dormitories.id",ondelete="CASCADE"))
    rooms: Mapped[Optional[List["Room"]]] = relationship("Room", lazy="joined")

    def to_dto(self) -> FloorRead:
        return FloorRead.model_validate(self)
