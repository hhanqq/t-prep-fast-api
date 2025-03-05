from fastapi import APIRouter, Depends
from .services import QuestionService
from .schemas import Question
from .rb import RBQuestion

router = APIRouter(prefix='/questions', tags=['Список вопросов'])

@router.get('', summary='Получить все вопросы')
async def get_all_questions(request_body: RBQuestion = Depends()):
    return await QuestionService.find_all(**request_body.to_dict())


@router.post('/add/')
async def add_questions(qstn: Question) -> dict:
    check = await QuestionService.add(**qstn.model_dump())
    if check:
        return {'message': 'Вопросы успешно загружены'}
    else:
        return{'Error': "Ошибка при добавлении"}