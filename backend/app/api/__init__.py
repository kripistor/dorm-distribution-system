from fastapi import APIRouter

from app.api.v1 import dormitory, floor, room

api_router = APIRouter()

api_router.include_router(dormitory.router, tags=["dormitories"])
api_router.include_router(floor.router, tags=["floors"])
api_router.include_router(room.router, tags=["rooms"])
