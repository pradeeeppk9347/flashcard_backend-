
from pydantic import BaseModel

class Flashcard(BaseModel):
    student_id: str
    question: str
    answer: str
