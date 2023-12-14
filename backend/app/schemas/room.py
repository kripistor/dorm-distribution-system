from pydantic import BaseModel, ConfigDict


class RoomCreate(BaseModel):
    floor_id: int
    capacity: int


class RoomUpdate(RoomCreate):
    pass


class RoomRead(RoomCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
