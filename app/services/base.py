from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import new_session 


class BaseService:
    model = None
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add(cls, **values):
        async with new_session() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance