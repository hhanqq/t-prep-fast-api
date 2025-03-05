from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String, index=True)
    description = Column(Text)
    test_code = Column(Text)
    unique_url = Column(String, unique=True, default=lambda: str(uuid.uuid4()))

    # Дополнительные поля и связи, если нужно
