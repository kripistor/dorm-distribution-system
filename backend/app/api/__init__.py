from fastapi import APIRouter

from app.api.v1 import dormitory

api_router = APIRouter()

api_router.include_router(dormitory.router, tags=["dormitories"])
