from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from routers import auth

app = FastAPI(title="Auth API")
PORT = 8080

origins = [f"http://localhost:{PORT}"]  # Домен вашего фронтенда

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршрут авторизации
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "API is running"}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
