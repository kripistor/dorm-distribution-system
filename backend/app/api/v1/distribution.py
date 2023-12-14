from typing import Any, List
from uuid import UUID

from fastapi import APIRouter

from app.deps.db import CurrentAsyncSession
from app.repo.distribution_repo import DistributionRepo
from app.schemas.person_attached_room import PersonAttachedRoomRead
from app.schemas.user_profile import UserUUID

router = APIRouter(prefix="/distributions")


@router.post("/{dormitory_id}", response_model=List[PersonAttachedRoomRead])
async def student_distribution(
    user_list: UserUUID,
    dormitory_id: int,
    session: CurrentAsyncSession,
) -> Any:
    distribution_repo: DistributionRepo = DistributionRepo(session)
    result = await distribution_repo.student_distribution(
        user_list.user_ids, dormitory_id
    )
    return result
