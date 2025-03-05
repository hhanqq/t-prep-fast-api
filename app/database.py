from multiprocessing import get_context
from datetime import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr


DB_HOST = 'localhost'
DB_PORT = '5433'
DB_NAME = 'postgres_db'
DB_USER = 'SU'
DB_PASSWORD = 'SU_passw'


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True, nullable=False)


class QuestionModel(Base):
    __tablename__ = 'Question'
    
    group_id: Mapped[int] = mapped_column(ForeignKey('Question_group.id'))
    qstn: Mapped[str]
    r_answr: Mapped[str]
    wr_answr1: Mapped[str]
    wr_answr2: Mapped[str]
    wr_answr3: Mapped[str]
    
    group = relationship('QGroupModel', back_populates='questions')
    
    
class QGroupModel(Base):
    __tablename__ = 'Question_group'
    
    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('User.id'))
    created_at: Mapped[datetime] = mapped_column(server_default = func.now(), onupdate=datetime.now)
    
    questions = relationship('QuestionModel', back_populates='group')
    user = relationship('UserModel', back_populates='groups')
    

class UserModel(Base):
    __tablename__ = 'User'
    
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    _password: Mapped[str]  # Хранит хэшированный пароль
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = get_context.hash(value)

    groups = relationship('QGroupModel', back_populates='user')