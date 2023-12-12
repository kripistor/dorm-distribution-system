import logging
from typing import List

from sqlalchemy import select, delete

from app.models.room import Room
from app.repo.repo import SQLAlchemyRepo
from app.schemas.room import RoomCreate, RoomUpdate


class RoomRepo(SQLAlchemyRepo):

    async def get_room_by_floor_id(self, floor_id: int) -> List[Room]:
        return (
            await self.session.execute(
                select(Room)
                .where(Room.floor_id == floor_id)
            )
        ).scalars().all()

    async def get_room(self, room_id: int| None = None, floor_id:int|None = None) -> Room:
        stmt = select(Room)
        if room_id:
            stmt = stmt.where(Room.id == room_id)
        if floor_id:
            stmt = stmt.where(Room.floor_id == floor_id)
        return (
            await self.session.execute(
                stmt
            )
        ).scalar()

    async def create_room(self, room_in: RoomCreate) -> Room:
        try:
            room = Room(**room_in.dict())
            self.session.add(room)
            await self.session.commit()
            return room
        except Exception as e:
            logging.error(f"Error creating room: {e}")
            await self.session.rollback()

    async def update_room(self, room_id: int, room_in: RoomUpdate) -> Room:
        room = await self.get_room_by_id(room_id)
        update_data = room_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(room, field, value)
        await self.session.commit()
        return room

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
