from fastapi import APIRouter 
from sqlalchemy import select 
from database import new_session 
from models.user import QuestionModel

router = APIRouter(prefix='/questions', tags=['Список вопросов'])

@router.get('/', summary='Получить все вопросы')
async def get_all_users():
    async with new_session() as session:
        query = select(QuestionModel)
        result = await session.execute(query)
        users = result.scalars().all()
        return users