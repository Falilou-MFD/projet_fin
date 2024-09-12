from sqlalchemy.orm import Session
from models.subject_model import Subject
from schemas.subject_schema import SubjectCreate

def create_subject(db: Session, subject: SubjectCreate):
    db_subject = Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def get_subject_by_id(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()

def get_all_subjects(db: Session):
    return db.query(Subject).all()

def update_subject(db: Session, subject_id: int, updated_subject: SubjectCreate):
    subject = get_subject_by_id(db, subject_id)
    if subject:
        for key, value in updated_subject.dict().items():
            setattr(subject, key, value)
        db.commit()
        db.refresh(subject)
    return subject

def delete_subject(db: Session, subject_id: int):
    subject = get_subject_by_id(db, subject_id)
    if subject:
        db.delete(subject)
        db.commit()
    return subject
