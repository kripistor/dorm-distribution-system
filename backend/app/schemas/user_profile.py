from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


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


class UserProfileUpdate(UserProfileCreate):
    pass


class UserProfileRead(UserProfileCreate):
    id: int
    user_id: UUID

    class Config:
        model_config = ConfigDict(from_attributes=True)


class UserUUID(BaseModel):
    user_ids: list[UUID]
