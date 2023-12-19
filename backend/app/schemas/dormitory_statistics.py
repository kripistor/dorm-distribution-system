from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class FloorStatistics(BaseModel):
    floor_id: int
    floor_name: str
    occupied_space: int
    total_space: int
    rooms_free: int
    model_config = ConfigDict(from_attributes=True)


class DormitoryStatistics(BaseModel):
    dorm_id: int
    dorm_name: str
    dorm_address: str
    occupied_space: int
    total_space: int
    floors: Optional[List[FloorStatistics]] = None

    model_config = ConfigDict(from_attributes=True)
