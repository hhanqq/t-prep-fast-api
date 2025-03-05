from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class User(Base):
    __tablename__ = 'User'
    
    username: Mapped[str] = mapped_column(unique=True, nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)# Хранит хэшированный пароль

    # groups = relationship('QGroupModel', back_populates='user')
    

class QuestionModel(Base):
    __tablename__ = 'Question'
    
    # group_id: Mapped[int] = mapped_column(ForeignKey('Question_group.id'))
    qstn: Mapped[str]
    r_answr: Mapped[str]
    wr_answr1: Mapped[str]
    wr_answr2: Mapped[str]
    wr_answr3: Mapped[str]
    
    # group = relationship('QGroupModel', back_populates='questions')
    
    
class QGroupModel(Base):
    __tablename__ = 'Question_group'
    
    title: Mapped[str]
    # user_id: Mapped[int] = mapped_column(ForeignKey('User.id'))
    created_at: Mapped[datetime] = mapped_column(server_default = func.now(), onupdate=datetime.now)
    
    # questions = relationship('QuestionModel', back_populates='group')
    # user = relationship('User', back_populates='groups')  
