from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.schemas.person_attached_room import PersonAttachedRoomRead


class UserProfileCreate(BaseModel):
    user_id: UUID
    card_number: str
    name: str
    birth_date: datetime
    phone: str
    grant_order_number: str
    transfer_order_number: str
    transfer_date: datetime
    birth_place: str
    address: str
    concession: bool
    gender: str
    course: int


class UserProfileUpdate(UserProfileCreate):
    pass


class UserProfileRead(UserProfileCreate):
    id: int
    user_id: UUID
    room_distribution: Optional[PersonAttachedRoomRead] = None

    model_config = ConfigDict(from_attributes=True)


class UserUUID(BaseModel):
    user_ids: list[UUID]
