from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, test  # Если есть маршруты, добавляем

app = FastAPI(title="Auth API")

# Создаем таблицы в БД (если их нет)
Base.metadata.create_all(bind=engine)

# Подключаем маршруты
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(test.router)


@app.get("/")
def root():
    return {"message": "API is running"}
