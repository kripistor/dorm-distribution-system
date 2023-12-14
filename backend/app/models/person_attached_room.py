from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.schemas.person_attached_room import PersonAttachedRoomRead


class PersonAttachedRoom(Base):
    __tablename__ = "person_attached_rooms"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    room_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("rooms.id", ondelete="CASCADE")
    )

    def to_dto(self) -> PersonAttachedRoomRead:
        return PersonAttachedRoomRead.model_validate(self)
