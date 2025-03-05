from fastapi import FastAPI
import uvicorn


# from database import new_session
# from routers import auth, test  # Если есть маршруты, добавляем
from questions.router import router as router_users

app = FastAPI(title="Auth API")

# Создаем таблицы в БД (если их нет)
# Base.metadata.create_all(bind=engine)

# Подключаем маршруты
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(test.router)


@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(router_users)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)