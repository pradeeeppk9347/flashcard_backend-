
from fastapi import FastAPI
from typing import List
from random import shuffle

from models import Flashcard
from subject_inference import infer_subject
from data_store import flashcard_db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Flashcard API!"}

@app.post("/flashcard")
def add_flashcard(flashcard: Flashcard):
    subject = infer_subject(flashcard.question)
    flashcard_db.append({
        "student_id": flashcard.student_id,
        "question": flashcard.question,
        "answer": flashcard.answer,
        "subject": subject
    })
    return {"message": "Flashcard added successfully", "subject": subject}

@app.get("/get-subject")
def get_flashcards(student_id: str, limit: int = 5):
    student_cards = [card for card in flashcard_db if card["student_id"] == student_id]
    subject_groups = {}
    for card in student_cards:
        subject_groups.setdefault(card["subject"], []).append(card)
    mixed = [cards[0] for cards in subject_groups.values()]
    shuffle(mixed)
    return mixed[:limit]
