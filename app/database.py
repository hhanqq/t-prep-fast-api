from multiprocessing import get_context
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, relationship


DATABASE_URL = "postgresql://user:password@localhost:8088/dbname"

engine = create_engine(DATABASE_URL)
new_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    pass


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
    user_id: Mapped[int] = mapped_column(unique=True)
    
    questions = relationship('QuestionModel', back_populates='group')
    

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
    