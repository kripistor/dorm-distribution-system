from typing import List
from uuid import UUID

from sqlalchemy import select

from app.models import UserProfile, PersonAttachedRoom
from app.repo.dormitory_repo import DormitoryRepo
from app.repo.repo import SQLAlchemyRepo


class DistributionRepo(SQLAlchemyRepo):
    async def student_distribution(
        self, user_ids: List[UUID], dormitory_id: int
    ) -> List[PersonAttachedRoom]:
        dormitory_repo: DormitoryRepo = DormitoryRepo(self.session)
        dormitory = await dormitory_repo.get_by_id(dormitory_id)
        floors = sorted(dormitory.floors, key=lambda floor: floor.id)
        rooms = [
            room
            for floor in floors
            for room in sorted(floor.rooms, key=lambda room: room.id)
        ]

        # Retrieve and sort the users
        users = await self.session.execute(
            select(UserProfile).where(UserProfile.user_id.in_(user_ids))
        )
        users = sorted(
            users.scalars().all(), key=lambda user: user.concession, reverse=True
        )

        person_attached_rooms = []
        for user in users:
            # Find a suitable room for the user
            for room in rooms:
                occupants = await self.session.execute(
                    select(PersonAttachedRoom).where(
                        PersonAttachedRoom.room_id == room.id
                    )
                )
                occupants = occupants.scalars().all()

                if len(occupants) < room.capacity:
                    # The room is not full and either empty or contains users of the same gender as the current user
                    for occupant in occupants:
                        occupant_user_profile = await self.session.execute(
                            select(UserProfile).where(
                                UserProfile.user_id == occupant.user_id
                            )
                        )
                        occupant_user_profile = occupant_user_profile.scalars().one()
                        if occupant_user_profile.gender != user.gender:
                            break
                    else:
                        # Check if the user is already in a room
                        existing_room = await self.session.execute(
                            select(PersonAttachedRoom).where(
                                PersonAttachedRoom.user_id == user.user_id
                            )
                        )
                        existing_room = existing_room.scalars().first()
                        if existing_room is not None:
                            # The user is already in a room, skip to the next user
                            break

                        person_attached_room = PersonAttachedRoom(
                            user_id=user.user_id, room_id=room.id
                        )
                        self.session.add(person_attached_room)
                        await self.session.commit()
                        person_attached_rooms.append(person_attached_room)
                        break
            else:
                raise Exception(f"No suitable room found for user {user.user_id}")

        return person_attached_rooms
