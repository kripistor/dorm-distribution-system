from typing import Any, List

from fastapi import APIRouter, HTTPException
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.models.dormitory import Dormitory
from app.repo.dormitory_repo import DormitoryRepo
from app.schemas.dormitory import DormitoryRead, DormitoryCreate, DormitoryUpdate
from app.schemas.dormitory_statistics import DormitoryStatistics

router = APIRouter(prefix="/dormitories")


@router.get("", response_model=List[DormitoryRead])
async def get_dormitories(
    response: Response,
    session: CurrentAsyncSession,
    request_params: ItemRequestParams,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    dormitories = await dormitory_repo.get_all()
    if not dormitories:
        return []
    return dormitories


@router.get("/all_stats", response_model=List[DormitoryStatistics])
async def get_dormitories_statistic(
    session: CurrentAsyncSession,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    dormitories = await dormitory_repo.get_all_dormitories_statistics()
    return dormitories


@router.get("/{dormitory_id}", response_model=DormitoryRead)
async def get_dormitory(
    dormitory_id: int,
    session: CurrentAsyncSession,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    dormitory = await dormitory_repo.get_by_id(dormitory_id)
    if not dormitory:
        raise HTTPException(status_code=404, detail="Dormitory not found")
    return dormitory


@router.post("", response_model=DormitoryRead, status_code=201)
async def create_dormitory(
    dormitory_in: DormitoryCreate,
    session: CurrentAsyncSession,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    dormitory = Dormitory(**dormitory_in.model_dump())
    result = await dormitory_repo.create(dormitory)
    return result


@router.get("/stats/{dormitory_id}", response_model=DormitoryStatistics)
async def get_dormitory_statistic(
    dormitory_id: int,
    session: CurrentAsyncSession,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    dormitory = await dormitory_repo.get_dormitory_statistics_by_id(dormitory_id)
    return dormitory


@router.put("/{dormitory_id}", response_model=DormitoryRead)
async def update_dormitory(
    dormitory_id: int,
    dormitory_in: DormitoryUpdate,
    session: CurrentAsyncSession,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    result = await dormitory_repo.update(dormitory_id, dormitory_in)
    return result


@router.delete("/{dormitory_id}")
async def delete_dormitory(
    dormitory_id: int,
    session: CurrentAsyncSession,
) -> Any:
    dormitory_repo: DormitoryRepo = DormitoryRepo(session)
    result = await dormitory_repo.delete(dormitory_id)
    return result
