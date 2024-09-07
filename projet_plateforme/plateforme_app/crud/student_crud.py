from sqlalchemy.orm import Session
from models.student_model import Student
from schemas.student_schema import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_by_num_etu(db: Session, num_etu: str):
    return db.query(Student).filter(Student.num_etu == num_etu).first()

def get_all_students(db: Session):
    return db.query(Student).all()

def update_student(db: Session, num_etu: str, updated_student: StudentCreate):
    student = get_student_by_num_etu(db, num_etu)
    if student:
        for key, value in updated_student.dict().items():
            setattr(student, key, value)
        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, num_etu: str):
    student = get_student_by_num_etu(db, num_etu)
    if student:
        db.delete(student)
        db.commit()
    return student
