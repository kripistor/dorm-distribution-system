import logging
from typing import List

from sqlalchemy import select, delete

from app.models.floor import Floor
from app.repo.repo import SQLAlchemyRepo
from app.schemas.floor import FloorCreate, FloorUpdate


class FloorRepo(SQLAlchemyRepo):
    async def get_floor_by_dormitory_id(self, dormitory_id: int) -> List[Floor]:
        return (
            await self.session.execute(
                select(Floor)
                .where(Floor.dormitory_id == dormitory_id)
            )
        ).unique().scalars().all()

    async def get_floor_by_id(self, floor_id: int) -> Floor:
        return (
            await self.session.execute(
                select(Floor)
                .where(Floor.id == floor_id)
            )
        ).scalar()

    async def create_floor(self, floor_in: Floor) -> Floor:
        try:
            self.session.add(floor_in)
            await self.session.commit()
            return floor_in
        except Exception as e:
            await self.session.rollback()

    async def update_floor(self, floor_id: int, floor_in: FloorUpdate) -> Floor:
        floor = await self.get_floor_by_id(floor_id)
        update_data = floor_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(floor, field, value)
        await self.session.commit()
        return floor

    async def delete_floor(self, floor_id: int) -> None:
        stmt = delete(Floor).where(
            Floor.id == floor_id
        )
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logging.error(f"Error deleting floor: {e}")
            await self.session.rollback()