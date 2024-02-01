from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

app = FastAPI()
'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/quizzes/{quiz_id}")
async def get_quiz_details(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    questions = db.query(Question).filter(Question.quiz_id == quiz_id).all()
    options = db.query(Option).filter(Option.question_id.in_([q.question_id for q in questions])).all()
    return {"quiz": quiz, "questions": questions, "options": options}

@app.post("/submit")
async def submit_answers(answers: dict, quiz_id: int = Query(..., ge=1), db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    # Validate user input (ensure valid question IDs and option IDs)
    # ...

    attempt = UserAttempt(quiz_id=quiz_id, start_time=datetime.now())  # Add user_id if available
    db.add(attempt)
    db.commit()

    # Process answers, store in Answer table, update attempt_no, etc.
    # ...

    return {"message": "Answers submitted successfully"}

@app.get("/result/{quiz_id}")
async def get_quiz_result(quiz_id: int, db: Session = Depends(get_db)):
    # Retrieve quiz result, calculate score, show correct answers
    # ...

    return {"score": score, "correct_answers": correct_answers}
'''