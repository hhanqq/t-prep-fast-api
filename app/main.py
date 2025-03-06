from fastapi import FastAPI
import uvicorn
from routers import auth

app = FastAPI(title="Auth API")

# Подключаем маршрут авторизации
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "API is running"}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
