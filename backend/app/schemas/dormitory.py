from pydantic import BaseModel


class DormitoryCreate(BaseModel):
    name: str
    address: str


class DormitoryUpdate(DormitoryCreate):
    pass


class Dormitory(DormitoryCreate):
    id: int

    class Config:
        orm_mode = True
