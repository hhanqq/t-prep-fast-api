from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.test import Test
from app.schemas.test import TestCreate  # Создайте схему для создания тестов

router = APIRouter()

@router.post("/create-test/")
def create_test(test: TestCreate, db: Session = Depends(get_db)):
    # Создаем новый тест
    new_test = Test(test_name=test.test_name, description=test.description, test_code=test.test_code)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)

    # Генерация ссылки для доступа к тесту
    test_url = f"http://127.0.0.1:8000/test/{new_test.unique_url}"
    return {"message": "Тест создан", "test_url": test_url}


@router.get("/test/{unique_url}")
def get_test_by_url(unique_url: str, db: Session = Depends(get_db)):
    # Ищем тест по уникальной ссылке
    test = db.query(Test).filter(Test.unique_url == unique_url).first()
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")

    # Возвращаем информацию о тесте
    return {"test_name": test.test_name, "description": test.description, "test_code": test.test_code}
