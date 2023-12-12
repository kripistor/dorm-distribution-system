from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from app.schemas.dormitory import DormitoryRead
from app.schemas.floor import FloorRead
from app.schemas.person_attached_room import PersonAttachedRoomRead
from app.schemas.room import RoomRead


class DormitoryStatistics(BaseModel):
    dormitory_id: Optional[List[DormitoryRead]] = None
    floors: Optional[List[FloorRead]] = None
    rooms: Optional[List[RoomRead]] = None
    person_attached_rooms: Optional[List[PersonAttachedRoomRead]] = None

    model_config = ConfigDict(from_attributes=True)
