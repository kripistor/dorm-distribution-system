from typing import Any, List

from fastapi import APIRouter
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.repo.floor_repo import FloorRepo
from app.models.floor import Floor
from app.schemas.floor import FloorRead, FloorUpdate, FloorCreate

router = APIRouter(prefix="/floors")


@router.get("/{dormitory_id}", response_model=List[FloorRead])
async def get_dormitory_floor(
    dormitory_id: int,
    response: Response,
    session: CurrentAsyncSession,
    request_params: ItemRequestParams,
) -> Any:
    floor_repo: FloorRepo = FloorRepo(session)
    floors = await floor_repo.get_floor_by_dormitory_id(dormitory_id)
    if not floors:
        return []
    return floors


@router.post("", response_model=FloorRead, status_code=201)
async def create_floor(
    floor_in: FloorCreate,
    session: CurrentAsyncSession,
) -> Any:
    floor_repo: FloorRepo = FloorRepo(session)
    floor = Floor(**floor_in.model_dump())
    result = await floor_repo.create_floor(floor)
    return result


@router.put("/{floor_id}", response_model=FloorRead)
async def update_floor(
    floor_id: int,
    floor_in: FloorUpdate,
    session: CurrentAsyncSession,
) -> Any:
    floor_repo: FloorRepo = FloorRepo(session)
    result = await floor_repo.update_floor(floor_id, floor_in)
    return result


@router.delete("/{floor_id}")
async def delete_floor(
    floor_id: int,
    session: CurrentAsyncSession,
) -> Any:
    floor_repo: FloorRepo = FloorRepo(session)
    result = await floor_repo.delete_floor(floor_id)
    return result
