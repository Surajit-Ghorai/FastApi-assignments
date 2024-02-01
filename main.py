from fastapi import FastAPI, HTTPException, Query, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Session_local
from models import *

def get_db():
    db= Session_local()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

#class BaseModel(BaseModel):
#    class Config:
#        orm_mode = True

class QuizRequest(BaseModel):
    quiz_id: int

class SubmitRequest(BaseModel):
    quiz_id: int
    user_answers: dict

class QuizResult(BaseModel):
    score: int
    correct_answers: dict

@app.get("/quizzes/{course_id}/{quiz_id}")
async def get_quiz(course_id: int, quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    db.close()
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz.questions

@app.post("/submit")
async def submit_quiz(submit_request: SubmitRequest):
    # Validate user input

    # Calculate score
    return

@app.get("/result")
async def get_result():
    return

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
