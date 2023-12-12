import logging
from typing import List

from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError

from app.models import Floor
from app.models.dormitory import Dormitory
from app.repo.repo import SQLAlchemyRepo
from app.schemas.dormitory import DormitoryCreate, DormitoryUpdate
from app.schemas.dormitory_statistics import DormitoryStatistics


class DormitoryRepo(SQLAlchemyRepo):
    async def get_all(self) -> List[Dormitory]:
        return (
            await self.session.execute(
                select(Dormitory)
            )
        ).scalars().all()

    async def get_by_id(self, dormitory_id: int) -> Dormitory:
        return (
            await self.session.execute(
                select(Dormitory)
                .where(Dormitory.id == dormitory_id)
            )
        ).scalar()

    async def create(self, dormitory_in: Dormitory) -> Dormitory:
        try:
            self.session.add(dormitory_in)
            await self.session.commit()
            return dormitory_in
        except Exception as e:
            await self.session.rollback()

    async def update(self, dormitory_id: int, dormitory_in: DormitoryUpdate) -> Dormitory:
        dormitory: Dormitory = await self.get_by_id(dormitory_id)
        update_data = dormitory_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(dormitory, field, value)
        await self.session.commit()
        return dormitory

    async def delete(self, dormitory_id: int) -> None:
        stmt = delete(Dormitory).where(
            Dormitory.id == dormitory_id
        )
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logging.error(f"Error deleting dormitory: {e}")
            await self.session.rollback()

    async def get_dormitory_statistic_by_id(self, dormitory_id: int):
        query = await self.session.execute(
            select(Dormitory).where(Dormitory.id == dormitory_id)
        )
        dormitory_statistic = query.scalar()
        return DormitoryStatistics.model_validate(dormitory_statistic) if dormitory_statistic else None

