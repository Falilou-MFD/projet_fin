from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models import student_model
from projet_plateforme.plateforme_app.crud import student_crud
from projet_plateforme.plateforme_app.schemas import student_schema
from . import models, schemas, crud
from projet_plateforme.plateforme_app.database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/{num_etu}", response_model=schemas.Student)
def fetch_student_by_num(num_etu: str, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_num(db, num_etu=num_etu)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student