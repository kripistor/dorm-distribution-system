from pydantic import BaseModel, ConfigDict


class FloorCreate(BaseModel):
    name: str
    dormitory_id: int


class FloorUpdate(FloorCreate):
    pass


class Floor(FloorCreate):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
