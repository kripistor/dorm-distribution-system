from typing import Any, List

from fastapi import APIRouter, HTTPException
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.models.person_attached_room import PersonAttachedRoom
from app.repo.person_attached_room_repo import PersonAttachedRoomRepo
from app.repo.room_repo import RoomRepo
from app.schemas.person_attached_room import (
    PersonAttachedRoomRead,
    PersonAttachedRoomCreate,
)

router = APIRouter(prefix="/person_attached_rooms")


@router.get("", response_model=List[PersonAttachedRoomRead])
async def get_all_person_attached_rooms(
    response: Response,
    session: CurrentAsyncSession,
    request_params: ItemRequestParams,
) -> Any:
    person_attached_room_repo: PersonAttachedRoomRepo = PersonAttachedRoomRepo(session)
    person_attached_rooms = await person_attached_room_repo.get_all()
    if not person_attached_rooms:
        return []
    return person_attached_rooms


@router.get("/", response_model=List[PersonAttachedRoomRead])
async def get_person_attached_rooms(
    response: Response,
    session: CurrentAsyncSession,
    request_params: ItemRequestParams,
    user_id: int | None = None,
    room_id: int | None = None,
) -> Any:
    person_attached_room_repo: PersonAttachedRoomRepo = PersonAttachedRoomRepo(session)
    person_attached_rooms = await person_attached_room_repo.get_by_id(
        user_id=user_id, room_id=room_id
    )
    if not person_attached_rooms:
        return []
    return person_attached_rooms


@router.post("", response_model=PersonAttachedRoomRead, status_code=201)
async def create_person_attached_room(
    person_attached_room_in: PersonAttachedRoomCreate,
    session: CurrentAsyncSession,
) -> Any:
    person_attached_room_repo: PersonAttachedRoomRepo = PersonAttachedRoomRepo(session)
    room_repo: RoomRepo = RoomRepo(session)

    person_attached_room = PersonAttachedRoom(**person_attached_room_in.model_dump())
    room = room_repo.occupancy_result(person_attached_room)
    if room:
        raise HTTPException(status_code=400, detail="The room is full")
    result = await person_attached_room_repo.create_person_attached_room(
        person_attached_room
    )
    return result


@router.delete("/")
async def delete_person_attached_room(
    session: CurrentAsyncSession,
    user_id: int | None = None,
    room_id: int | None = None,
) -> Any:
    person_attached_room_repo: PersonAttachedRoomRepo = PersonAttachedRoomRepo(session)
    result = await person_attached_room_repo.delete(user_id, room_id)
    return result
