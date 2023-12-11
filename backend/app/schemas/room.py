from pydantic import BaseModel

from pydantic import BaseModel


class RoomCreate(BaseModel):
    floor_id: int
    capacity: int


class RoomUpdate(RoomCreate):
    pass


class Room(RoomCreate):
    class Config:
        orm_mode = True
