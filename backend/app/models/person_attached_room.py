from uuid import UUID

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base
from app.schemas.person_attached_room import PersonAttachedRoomRead


class PersonAttachedRoom(Base):
    __tablename__ = "person_attached_rooms"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    room_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("rooms.id", ondelete="CASCADE")
    )
    room: Mapped["Room"] = relationship("Room", lazy="joined", foreign_keys=[room_id])

    def to_dto(self) -> PersonAttachedRoomRead:
        return PersonAttachedRoomRead.model_validate(self)
