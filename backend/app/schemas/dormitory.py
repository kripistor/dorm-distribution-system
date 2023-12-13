from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from app.schemas.floor import FloorRead
from app.schemas.person_attached_room import PersonAttachedRoomRead
from app.schemas.room import RoomRead


class DormitoryCreate(BaseModel):
    name: str
    address: str
    img: str


class DormitoryUpdate(DormitoryCreate):
    pass


class DormitoryRead(DormitoryCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class DormitoryStatistics(DormitoryRead):
    floors: Optional[List[FloorRead]] = None

    model_config = ConfigDict(from_attributes=True)
