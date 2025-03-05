class RBQuestion:
    def __init__(self, question_id:int | None = None, 
                 qstn:str | None = None,
                 correct_answr:str | None = None,
                 wr_answr1:str | None = None,
                 wr_answr2:str | None = None,
                 wr_answr3:str | None = None):
        self.id = question_id
        self.qstn = qstn
        self.correct_answr = correct_answr
        self.wr_answr1 = wr_answr1
        self.wr_answr2 = wr_answr2
        self.wr_answr3 = wr_answr3
        
    def to_dict(self) -> dict:
        data = {'id': self.id, 'question': self.qstn, 'correct_answer': self.correct_answer,
                'wrong_answer1': self.wr_answr1, 'wrong_answer2': self.wr_answr2, 
                'wrong_answer3': self.wr_answr3,}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data