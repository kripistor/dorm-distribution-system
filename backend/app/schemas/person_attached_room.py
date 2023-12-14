from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PersonAttachedRoomCreate(BaseModel):
    room_id: int
    user_id: UUID


class PersonAttachedRoomUpdate(PersonAttachedRoomCreate):
    pass


class PersonAttachedRoomRead(PersonAttachedRoomCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
