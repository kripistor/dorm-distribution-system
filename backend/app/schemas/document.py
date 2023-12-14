from pydantic import BaseModel


class FileInfo(BaseModel):
    filename: str
