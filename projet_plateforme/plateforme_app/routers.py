from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models import admin_model
from projet_plateforme.plateforme_app.crud import admin_crud
from projet_plateforme.plateforme_app.schemas import admin_schema
from . import models, schemas, crud
from projet_plateforme.plateforme_app.database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/admins", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admins/{num_admin}", response_model=schemas.Admin)
def fetch_admin_by_num(num_admin: str, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_num(db, num_admin=num_admin)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin


@app.post("/discussions", response_model=schemas.Discussion)
def create_discussion(discussion: schemas.DiscussionCreate, db: Session = Depends(get_db)):
    return crud.create_discussion(db=db, discussion=discussion)

@app.get("/discussions/{id}", response_model=schemas.Discussion)
def fetch_single_discussion(id: int, db: Session = Depends(get_db)):
    return crud.get_discussion(db, id=id)


@app.post("/forum/users", response_model=schemas.ForumUser)
def create_forum_user(forum_user: schemas.ForumUserCreate, db: Session = Depends(get_db)):
    return crud.create_forum_user(db=db, forum_user=forum_user)

@app.get("/forum/users/{id}", response_model=schemas.ForumUser)
def fetch_forum_user(id: int, db: Session = Depends(get_db)):
    return crud.get_forum_user(db, id=id)


@app.post("/messages", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/{discussion_id}", response_model=list[schemas.Message])
def fetch_discussion_messages(discussion_id: int, db: Session = Depends(get_db)):
    return crud.get_discussion_messages(db, discussion_id=discussion_id)


@app.post("/profiles", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)

@app.get("/profiles/{id}", response_model=schemas.Profile)
def fetch_single_profile(id: int, db: Session = Depends(get_db)):
    return crud.get_profile(db, id=id)


@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/{num_etu}", response_model=schemas.Student)
def fetch_student_by_num(num_etu: str, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_num(db, num_etu=num_etu)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/subjects", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, subject=subject)

@app.get("/subjects/{id}", response_model=schemas.Subject)
def fetch_single_subject(id: int, db: Session = Depends(get_db)):
    return crud.get_subject(db, id=id)