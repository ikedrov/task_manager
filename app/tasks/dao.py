from sqlalchemy import and_, insert, select, update
from sqlalchemy.exc import SQLAlchemyError

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.logger import logger
from app.tasks.models import Tasks


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def get_tasks_for_user(cls, user_id: int):
        async with async_session_maker() as session:
            try:
                query = select(Tasks.__table__.columns).where(Tasks.owner_id == user_id)
                result = await session.execute(query)
                return result.mappings().all()
            except:
                return None

    @classmethod
    async def add(cls, owner_id: int, title: str, description: str, completed: bool):
        async with async_session_maker() as session:
            try:
                add_task = (
                    insert(Tasks)
                    .values(
                        owner_id=owner_id,
                        title=title,
                        description=description,
                        completed=completed,
                    )
                    .returning(Tasks)
                )
                new_task = await session.execute(add_task)
                await session.commit()
                return new_task.scalar()

            except (SQLAlchemyError, Exception) as e:
                if isinstance(e, SQLAlchemyError):
                    msg = "Database Exc: Cannot add task"
                elif isinstance(e, Exception):
                    msg = "Unknown Exc: Cannot add task"
                extra = {
                    "owner_id": owner_id,
                    "title": title,
                    "description": description,
                    "completed": completed,
                }
                logger.error(msg, extra=extra, exc_info=True)
                # except:
                return None

    @classmethod
    async def update(cls, owner_id: int, task_id: int, completed: bool):
        async with async_session_maker() as session:
            try:
                stmt = (
                    update(Tasks)
                    .where(and_(Tasks.owner_id == owner_id, Tasks.id == task_id))
                    .values(completed=completed)
                    .returning(Tasks)
                )
                updated_task = await session.execute(stmt)
                await session.commit()
                return updated_task.scalar()
            except:
                return None
