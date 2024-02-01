from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
#from sqlalchemy.orm import relationship

from database import Base, engine

def create_tables():
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String)
    description = Column(String)

class Quiz(Base):
    __tablename__ = "quizzes"
    quiz_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    time_limit = Column(Integer)
    attempts_allowed = Column(Integer)
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    #course = relationship("Course", back_populates="quizzes")

class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    question_type = Column(String, default='mcq')
    problem_desc = Column(String)
    marks = Column(Integer)
    quiz_id = Column(Integer, ForeignKey("quizzes.quiz_id"))
    #quiz = relationship("Quiz", back_populates="questions")

class Option(Base):
    __tablename__ = "options"
    option_id = Column(Integer, primary_key=True, autoincrement=True)
    option_desc = Column(String)
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    #question = relationship("Question", back_populates="options")

class Answer(Base):
    __tablename__ = "answers"
    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    attempt_id = Column(Integer, ForeignKey("user_attempts.attempt_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    option_id = Column(Integer, ForeignKey("options.option_id"))

class UserAttempt(Base):
    __tablename__ = "user_attempts"
    attempt_id = Column(Integer, primary_key=True, autoincrement=True)
    attempt_no = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.quiz_id"))
    #user = relationship("User", back_populates="attempts")
    #quiz = relationship("Quiz", back_populates="attempts")