from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from multiprocessing import get_context
from datetime import datetime
from typing import Annotated


DB_HOST = 'localhost'
DB_PORT = '5433'
DB_NAME = 'postgres_db'
DB_USER = 'SU'
DB_PASSWORD = 'SU_passw'


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

