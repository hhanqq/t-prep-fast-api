from pydantic import BaseModel

class TestCreate(BaseModel):
    test_name: str
    description: str
    test_code: str

    class Config:
        orm_mode = True
