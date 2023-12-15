from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.schemas.room import RoomRead


class PersonAttachedRoomCreate(BaseModel):
    room_id: int | None = None
    user_id: UUID | None = None


class PersonAttachedRoomUpdate(PersonAttachedRoomCreate):
    pass


class PersonAttachedRoomRead(PersonAttachedRoomCreate):
    id: int | None = None
    room: Optional[RoomRead] = None

    model_config = ConfigDict(from_attributes=True)
