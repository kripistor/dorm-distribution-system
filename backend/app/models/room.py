from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Room(Base):
    __tablename__ = "rooms"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    floor_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("floors.id", ondelete="CASCADE")
    )
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
