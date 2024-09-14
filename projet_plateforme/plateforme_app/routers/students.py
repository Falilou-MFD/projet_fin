from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import student_model
from .. import crud_def as crud
from ..schemas.student_schema import *
from ..schemas.student_schema import *
from ..database import SessionLocal, engine
from typing import List
from .. import crud, schemas
from ..database import get_db

app = FastAPI()

@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)

@app.get("/students/", response_model=List[Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_students(db=db, skip=skip, limit=limit)

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db=db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
