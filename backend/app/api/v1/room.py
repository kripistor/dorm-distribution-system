from typing import Any, List

from fastapi import APIRouter
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.models import Room
from app.repo.room_repo import RoomRepo
from app.schemas.room import RoomRead, RoomUpdate, RoomCreate

router = APIRouter(prefix="/rooms")


@router.get("/", response_model=List[RoomRead])
async def get_floor_rooms(
        session: CurrentAsyncSession,
        floor_id: int | None = None,
        room_id: int | None = None,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    room = await room_repo.get_room(room_id=room_id, floor_id=floor_id)
    if not room:
        return []
    return room


@router.post("", response_model=RoomRead, status_code=201)
async def create_room(
        room_in: RoomCreate,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    room = Room(**room_in.model_dump())
    result = await room_repo.create_room(room)
    return result


@router.put("/{room_id}", response_model=RoomRead)
async def update_room(
        room_id: int,
        room_in: RoomUpdate,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    result = await room_repo.update_room(room_id, room_in)
    return result


@router.delete("/{room_id}")
async def delete_room(
        room_id: int,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    result = await room_repo.delete_room(room_id)
    return result
