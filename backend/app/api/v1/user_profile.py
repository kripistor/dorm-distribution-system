from typing import Any, List
from uuid import UUID

from fastapi import APIRouter
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.models.user_profile import UserProfile
from app.repo.user_profile_repo import UserProfileRepo
from app.schemas.user_profile import (
    UserProfileRead,
    UserProfileCreate,
    UserProfileUpdate,
)

router = APIRouter(prefix="/user_profiles")


@router.get("", response_model=List[UserProfileRead])
async def get_user_profiles(
    response: Response,
    session: CurrentAsyncSession,
    request_params: ItemRequestParams,
) -> Any:
    user_profile_repo: UserProfileRepo = UserProfileRepo(session)
    user_profiles = await user_profile_repo.get_all()
    if not user_profiles:
        return []
    return user_profiles


@router.post("", response_model=UserProfileRead, status_code=201)
async def create_user_profile(
    user_profile_in: UserProfileCreate,
    session: CurrentAsyncSession,
) -> Any:
    user_profile_repo: UserProfileRepo = UserProfileRepo(session)
    user_profile = UserProfile(**user_profile_in.model_dump())
    result = await user_profile_repo.create(user_profile)
    return result


@router.get("/{user_id}", response_model=UserProfileRead)
async def get_user_profile(
    user_id: UUID,
    session: CurrentAsyncSession,
) -> Any:
    user_profile_repo: UserProfileRepo = UserProfileRepo(session)
    result = await user_profile_repo.get_by_id(user_id)
    return result


@router.put("/{user_id}", response_model=UserProfileRead)
async def update_user_profile(
    user_id: UUID,
    user_profile_in: UserProfileUpdate,
    session: CurrentAsyncSession,
) -> Any:
    user_profile_repo: UserProfileRepo = UserProfileRepo(session)
    result = await user_profile_repo.update(user_id, user_profile_in)
    return result


@router.delete("/{user_id}")
async def delete_user_profile(
    user_id: UUID,
    session: CurrentAsyncSession,
) -> Any:
    user_profile_repo: UserProfileRepo = UserProfileRepo(session)
    await user_profile_repo.delete(user_id)
    return Response(status_code=204)
