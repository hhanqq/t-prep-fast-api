from pydantic import BaseModel, Field

class Question(BaseModel):
    id: int
    qstn: str = Field(min_lenght = 1, max_length=200, default='Вопросик')
    correct_answer: str = Field(min_lenght = 1, max_length=200)
    wr_answer1: str = Field(min_lenght = 1, max_length=200)
    wr_answer2: str = Field(min_lenght = 1, max_length=200)
    wr_answer3: str = Field(min_lenght = 1, max_length=200)
        