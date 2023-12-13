import logging
from typing import List

from sqlalchemy import select, delete, func

from app.models.person_attached_room import PersonAttachedRoom
from app.repo.repo import SQLAlchemyRepo
from app.schemas.person_attached_room import PersonAttachedRoomUpdate


class PersonAttachedRoomRepo(SQLAlchemyRepo):

    async def get_all(self) -> List[PersonAttachedRoom]:
        return (
            await self.session.execute(
                select(PersonAttachedRoom)
            )
        ).scalars().all()

    async def get_by_id(self, user_id: int | None = None, room_id: int | None = None) -> PersonAttachedRoom:
        stmt = select(PersonAttachedRoom)
        if user_id:
            stmt = stmt.where(PersonAttachedRoom.user_id == user_id)
        if room_id:
            stmt = stmt.where(PersonAttachedRoom.room_id == room_id)
        return (
            await self.session.execute(
                stmt
            )
        ).scalars().all()

    async def create_person_attached_room(self, person_attached_room_in: PersonAttachedRoom) -> PersonAttachedRoom:
        try:
            self.session.add(person_attached_room_in)
            await self.session.commit()
            return person_attached_room_in
        except Exception as e:
            await self.session.rollback()

    async def update(self, user_id, person_attached_room_in: PersonAttachedRoomUpdate) -> PersonAttachedRoom:
        person_attached_room: PersonAttachedRoom = await self.get_by_id(user_id)
        update_data = person_attached_room_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(person_attached_room, field, value)
        await self.session.commit()
        return person_attached_room

    async def delete(self, user_id: int | None = None, room_id: int | None = None) -> None:
        stmt = delete(PersonAttachedRoom)
        if user_id:
            stmt = stmt.where(PersonAttachedRoom.user_id == user_id)
        if room_id:
            stmt = stmt.where(PersonAttachedRoom.room_id == room_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logging.error(f"Error deleting person_attached_room: {e}")
            await self.session.rollback()

    async def count_people_per_room(self):
        result = (
            await self.session.query(
                PersonAttachedRoom.room_id, func.count(PersonAttachedRoom.id)
            )
            .group_by(PersonAttachedRoom.room_id)
            .all()
        )
        return result
