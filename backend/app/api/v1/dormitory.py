from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException
from sqlalchemy import func, select
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.models.dormitory import Dormitory
from app.schemas.dormitory import Dormitory as DormitoriesSchema, DormitoryCreate, DormitoryUpdate

router = APIRouter(prefix="/dormitories")


@router.get("", response_model=List[DormitoriesSchema])
async def get_dormitories(
        response: Response,
        session: CurrentAsyncSession,
        request_params: ItemRequestParams,
) -> Any:
    total = await session.scalar(
        select(func.count(Dormitory.id))
    )
    dormitories = (
        (
            await session.execute(
                select(Dormitory)
                .offset(request_params.skip)
                .limit(request_params.limit)
                .order_by(request_params.order_by)
            )
        )
        .scalars()
        .all()
    )
    return dormitories


@router.post("", response_model=DormitoriesSchema, status_code=201)
async def create_dormitory(
        dormitory_in: DormitoryCreate,
        session: CurrentAsyncSession,
) -> Any:
    dormitory = Dormitory(**dormitory_in.dict())
    session.add(dormitory)
    await session.commit()
    return dormitory


@router.put("/{dormitory_id}", response_model=DormitoriesSchema)
async def update_dormitory(
        dormitory_id: int,
        dormitory_in: DormitoryUpdate,
        session: CurrentAsyncSession,
) -> Any:
    dormitory: Optional[Dormitory] = await session.get(Dormitory, dormitory_id)
    if not dormitory:
        raise HTTPException(404)
    update_data = dormitory_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(dormitory, field, value)
    session.add(dormitory)
    await session.commit()
    return dormitory


@router.delete("/{dormitory_id}")
async def delete_dormitory(
        dormitory_id: int,
        session: CurrentAsyncSession,
) -> Any:
    dormitory: Optional[Dormitory] = await session.get(Dormitory, dormitory_id)
    if not dormitory:
        raise HTTPException(404)
    await session.delete(dormitory)
    await session.commit()
    return {"success": True}
