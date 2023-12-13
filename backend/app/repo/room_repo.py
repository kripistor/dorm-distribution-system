import logging
from typing import List

from sqlalchemy import select, delete, func

from app.models import PersonAttachedRoom, Floor
from app.models.room import Room
from app.repo.dormitory_repo import DormitoryRepo
from app.repo.floor_repo import FloorRepo
from app.repo.repo import SQLAlchemyRepo
from app.schemas.room import RoomUpdate


class RoomRepo(SQLAlchemyRepo):

    async def get_room(self, room_id: int | None = None, floor_id: int | None = None) -> List[Room]:
        stmt = select(Room)
        if room_id:
            stmt = stmt.where(Room.id == room_id)
        if floor_id:
            stmt = stmt.where(Room.floor_id == floor_id)
        return (
            await self.session.execute(
                stmt
            )
        ).scalars().all()

    async def create_room(self, room_in: Room) -> Room:
        try:
            self.session.add(room_in)
            await self.session.commit()
            return room_in
        except Exception as e:
            await self.session.rollback()

    async def update_room(self, room_id: int, room_in: RoomUpdate) -> Room:
        room = await self.get_room(room_id=room_id)
        update_data = room_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(room, field, value)
        await self.session.commit()
        return room

    async def occupancy_result(self, person_attached_room_in: PersonAttachedRoom):
        room_result = await self.session.execute(
            select(Room).where(Room.id == person_attached_room_in.room_id)
        )
        room = room_result.scalar_one()
        occupancy_result = await self.session.execute(
            select(func.count(PersonAttachedRoom.id)).filter(PersonAttachedRoom.room_id == room.id)
        )
        occupancy = occupancy_result.scalar_one()
        if occupancy == room.capacity:
            return True
        return False

    async def delete_room(self, room_id: int) -> None:
        stmt = delete(Room).where(
            Room.id == room_id
        )
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logging.error(f"Error deleting room: {e}")
            await self.session.rollback()
