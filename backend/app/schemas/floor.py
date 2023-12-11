from pydantic import BaseModel


class FloorCreate(BaseModel):
    name: str
    dormitory_id: int


class FloorUpdate(FloorCreate):
    pass


class Floor(FloorCreate):

    class Config:
        orm_mode = True
