from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import student_model
import crud_def as crud
from schemas.student_schema import *
from schemas.student_schema import *
from database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students", response_model= Student)
def create_student(student:  StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/{num_etu}", response_model= Student)
def fetch_student_by_num(num_etu: str, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_num(db, num_etu=num_etu)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
