from pydantic import BaseModel, ConfigDict


class DormitoryCreate(BaseModel):
    name: str
    address: str


class DormitoryUpdate(DormitoryCreate):
    pass


class DormitoryRead(DormitoryCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
