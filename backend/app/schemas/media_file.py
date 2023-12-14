from pydantic import BaseModel, ConfigDict


class AppMediaFileCreate(BaseModel):
    section_id: int
    filename: str
    short_tag: str


class AppMediaFileUpdate(AppMediaFileCreate):
    pass


class AppMediaFileRead(AppMediaFileCreate):
    id: int
    created_at: str
    updated_at: str

    model_config = ConfigDict(from_attributes=True)
