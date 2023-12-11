from typing import Any, List

from fastapi import APIRouter
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.repo.room_repo import RoomRepo
from app.schemas.room import Room as RoomSchema, RoomUpdate

router = APIRouter(prefix="/rooms")

@router.get("/{floor_id}", response_model=List[RoomSchema])
async def get_floor_rooms(
        floor_id: int,
        response: Response,
        session: CurrentAsyncSession,
        request_params: ItemRequestParams,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    rooms = await room_repo.get_room_by_floor_id(floor_id)
    if not rooms:
        return []
    return rooms

@router.post("", response_model=RoomSchema, status_code=201)
async def create_room(
        room_in: RoomSchema,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    room = RoomSchema(**room_in.dict())
    result = await room_repo.create_room(room)
    return result

@router.put("/{room_id}", response_model=RoomSchema)
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