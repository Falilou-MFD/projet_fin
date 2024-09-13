
from sqlalchemy.orm import Session
from models.student_model import Student
from schemas.student_schema import StudentCreate
from auth import get_password_hash
from .. import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.num_etu == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.num_etu == student_id).first()
    if db_student:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.num_etu == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student
