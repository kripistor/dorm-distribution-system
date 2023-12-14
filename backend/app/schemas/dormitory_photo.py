from pydantic import BaseModel, ConfigDict


class DormitoryPhotoCreate(BaseModel):
    dormitory_id: int
    img: str


class DormitoryPhotoUpdate(DormitoryPhotoCreate):
    pass


class DormitoryPhotoRead(DormitoryPhotoCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
