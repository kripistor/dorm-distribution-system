from fastapi import APIRouter

from app.api.v1 import (
    dormitory,
    floor,
    room,
    person_attached_room,
    user_profile,
    distribution,
    document,
)

api_router = APIRouter()

api_router.include_router(dormitory.router, tags=["dormitories"])
api_router.include_router(floor.router, tags=["floors"])
api_router.include_router(room.router, tags=["rooms"])
api_router.include_router(person_attached_room.router, tags=["person_attached_rooms"])
api_router.include_router(user_profile.router, tags=["user_profiles"])
api_router.include_router(distribution.router, tags=["distributions"])
api_router.include_router(document.router, tags=["documents"])
