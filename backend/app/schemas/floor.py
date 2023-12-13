from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from app.schemas.room import RoomRead


class FloorCreate(BaseModel):
    name: str
    dormitory_id: int


class FloorUpdate(FloorCreate):
    pass


class FloorRead(FloorCreate):
    id: int
    rooms: Optional[List[RoomRead]] = None
    model_config = ConfigDict(from_attributes=True)
