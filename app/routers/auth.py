from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.future import select

from schemas.user import UserCreate, Token
from models.user import User
from services.auth_service import hash_password, verify_password, create_access_token
from database import new_session

router = APIRouter()

@router.post("/register/")
async def register(user: UserCreate):
    async with new_session() as db:
        # Проверяем, есть ли уже пользователь с таким email
        result = await db.execute(select(User).where(User.email == user.email))
        existing_user = result.scalars().first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email уже зарегистрирован")

        # Хешируем пароль и создаем нового пользователя
        hashed_password = hash_password(user.password)
        new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)

        db.add(new_user)
        try:
            await db.commit()
            await db.refresh(new_user)
        except Exception:
            await db.rollback()
            raise HTTPException(status_code=500, detail="Ошибка при создании пользователя")

    return {"message": "Пользователь создан"}

@router.post("/login/", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    async with new_session() as db:
        # Ищем пользователя по email
        result = await db.execute(select(User).where(User.email == form_data.username))
        user = result.scalars().first()

        # Проверка пароля
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверные учетные данные")

        # Генерация токена
        access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
