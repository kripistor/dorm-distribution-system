import logging
from typing import List

from sqlalchemy import select, delete, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload, joinedload

from app.models import Room, Floor, PersonAttachedRoom
from app.models.dormitory import Dormitory
from app.repo.repo import SQLAlchemyRepo
from app.schemas.dormitory import DormitoryUpdate
from app.schemas.dormitory_statistics import DormitoryStatistics, FloorStatistics


class DormitoryRepo(SQLAlchemyRepo):
    async def get_all(self) -> List[Dormitory]:
        return (await self.session.execute(select(Dormitory))).scalars().all()

    async def get_by_id(self, dormitory_id: int) -> Dormitory:
        return (
            (
                await self.session.execute(
                    select(Dormitory)
                    .options(joinedload(Dormitory.floors))
                    .where(Dormitory.id == dormitory_id)
                )
            )
            .unique()
            .scalars()
            .one()
        )

    async def create(self, dormitory_in: Dormitory) -> Dormitory:
        try:
            self.session.add(dormitory_in)
            await self.session.commit()
            return dormitory_in
        except Exception as e:
            await self.session.rollback()

    async def update(
        self, dormitory_id: int, dormitory_in: DormitoryUpdate
    ) -> Dormitory:
        dormitory: Dormitory = await self.get_by_id(dormitory_id)
        update_data = dormitory_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(dormitory, field, value)
        await self.session.commit()
        return dormitory

    async def delete(self, dormitory_id: int) -> None:
        stmt = delete(Dormitory).where(Dormitory.id == dormitory_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logging.error(f"Error deleting dormitory: {e}")
            await self.session.rollback()

    async def get_dormitory_stats_by_id(self, dormitory_id: int):
        query = await self.session.execute(
            select(Dormitory)
            .options(
                selectinload(Dormitory.floors),
            )
            .where(Dormitory.id == dormitory_id)
        )
        dormitory_statistic = query.unique().scalars().all()
        print(dormitory_statistic)
        return (
            DormitoryStatistics.model_validate(dormitory_statistic[0])
            if dormitory_statistic
            else None
        )

    async def get_dormitory_statistics(self, dormitory_id: int) -> DormitoryStatistics:
        dormitory_result = await self.session.execute(
            select(Dormitory)
            .options(joinedload(Dormitory.floors))
            .filter_by(id=dormitory_id)
        )
        dormitory = dormitory_result.scalar()
        total_space_result = await self.session.execute(
            select(func.sum(Room.capacity))
            .join(Floor)
            .filter(Floor.dormitory_id == dormitory_id)
        )
        total_space = total_space_result.scalar()
        occupied_space_result = await self.session.execute(
            select(func.count(PersonAttachedRoom.id))
            .join(Room)
            .join(Floor)
            .filter(Floor.dormitory_id == dormitory_id)
        )
        occupied_space = occupied_space_result.scalar()

        floors = []
        dormitory = await self.session.merge(
            dormitory, options=joinedload(Dormitory.floors)
        )
        for floor in dormitory.floors:
            floor_total_space_result = await self.session.execute(
                select(func.sum(Room.capacity)).filter(Room.floor_id == floor.id)
            )
            floor_total_space = floor_total_space_result.scalar()
            if floor_total_space is None:
                floor_total_space = 0
            floor_occupied_space_result = await self.session.execute(
                select(func.count(PersonAttachedRoom.id))
                .join(Room)
                .filter(Room.floor_id == floor.id)
            )
            floor_occupied_space = floor_occupied_space_result.scalar()

            floor_rooms_free = 0
            for room in floor.rooms:
                room_occupancy_result = await self.session.execute(
                    select(func.count(PersonAttachedRoom.id)).filter(
                        PersonAttachedRoom.room_id == room.id
                    )
                )
                room_occupancy = room_occupancy_result.scalar()
                if room.capacity > room_occupancy:
                    floor_rooms_free += 1

            floors.append(
                FloorStatistics(
                    floor_id=floor.id,
                    floor_name=floor.name,
                    occupied_space=floor_occupied_space,
                    total_space=int(floor_total_space),
                    rooms_free=floor_rooms_free,
                )
            )

        return DormitoryStatistics(
            id=dormitory.id,
            dorm_id=dormitory.id,
            dorm_name=dormitory.name,
            dorm_address=dormitory.address,
            occupied_space=occupied_space,
            total_space=total_space,
            floors=floors,
        )
