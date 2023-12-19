import logging
from typing import List
from uuid import UUID

from sqlalchemy import select, delete

from app.models.person_attached_room import PersonAttachedRoom
from app.models.user_profile import UserProfile
from app.repo.repo import SQLAlchemyRepo
from app.schemas.user_profile import UserProfileUpdate


class UserProfileRepo(SQLAlchemyRepo):
    async def get_all(self) -> List[UserProfile]:
        # get all students, include info about their rooms
        stmt = await self.session.execute(
            select(UserProfile).order_by(UserProfile.name)
        )
        return stmt.scalars().all()

    async def get_by_id(self, user_id: UUID) -> UserProfile:
        return (
            (
                await self.session.execute(
                    select(UserProfile).where(UserProfile.user_id == user_id)
                )
            )
            .unique()
            .scalars()
            .one()
        )

    async def create(self, user_profile_in: UserProfile) -> UserProfile:
        try:
            self.session.add(user_profile_in)
            await self.session.commit()
            return user_profile_in
        except Exception as e:
            await self.session.rollback()

    async def update(
        self, user_id: UUID, user_profile_in: UserProfileUpdate
    ) -> UserProfile:
        user_profile: UserProfile = await self.get_by_id(user_id)
        update_data = user_profile_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user_profile, field, value)
        await self.session.commit()
        return user_profile

    async def delete(self, user_id: UUID) -> None:
        stmt = delete(UserProfile).where(UserProfile.user_id == user_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logging.error(f"Error deleting user_profile: {e}")
            await self.session.rollback()
