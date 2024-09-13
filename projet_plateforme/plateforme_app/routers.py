from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.admin_model import *
from crud.admin_crud import *
from schemas.admin_schema import *
from database import SessionLocal, engine
import crud_def as crud
from models.discussion_model import Discussion
from schemas.discussion_schema import DiscussionCreate
from models.forum_user_model import ForumUser
from schemas.forum_user_schema import ForumUserCreate
from models.message_model import Message
from schemas.message_schema import MessageCreate
from models.profile_model import Profile
from schemas.profile_schema import ProfileCreate
from models.subject_model import Subject
from schemas.subject_schema import SubjectCreate
from models.student_model import Student
from schemas.student_schema import StudentCreate
from . import schemas
from typing import List

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/admins", response_model=Admin)
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admins/{num_admin}", response_model=Admin)
def fetch_admin_by_num(num_admin: str, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_num(db, num_admin=num_admin)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin


@app.post("/discussions", response_model=Discussion)
def create_discussion(discussion: DiscussionCreate, db: Session = Depends(get_db)):
    return crud.create_discussion(db=db, discussion=discussion)

@app.get("/discussions/{id}", response_model=Discussion)
def fetch_single_discussion(id: int, db: Session = Depends(get_db)):
    return crud.get_discussion(db, id=id)


@app.post("/forum/users", response_model=ForumUserCreate)
def create_forum_user(forum_user: ForumUserCreate, db: Session = Depends(get_db)):
    return crud.create_forum_user(db=db, forum_user=forum_user)

# @app.get("/forum/users/{id}", response_model=ForumUser)
# def fetch_forum_user(id: int, db: Session = Depends(get_db)):
#     return crud.get_forum_user_by_id(db, id=id)

@app.get("/forum/users/{id}", response_model=(schemas.ForumUser))
def fetch_forum_user(id: int, db: Session = Depends(get_db)):
    db_forum_user = crud.get_forum_user(db, id=id)
    if not db_forum_user:
        raise HTTPException(status_code=404, detail="ForumUser not found")
    return db_forum_user

@app.post("/messages", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/{discussion_id}", response_model=list[Message])
def fetch_discussion_messages(discussion_id: int, db: Session = Depends(get_db)):
    return crud.get_discussion_messages(db, discussion_id=discussion_id)


@app.post("/profiles", response_model=Profile)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)

@app.get("/profiles/{id}", response_model=Profile)
def fetch_single_profile(id: int, db: Session = Depends(get_db)):
    return crud.get_profile(db, id=id)


@app.post("/students", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/{num_etu}", response_model=Student)
def fetch_student_by_num(num_etu: str, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_num(db, num_etu=num_etu)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/subjects", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, subject=subject)

@app.get("/subjects/{id}", response_model=Subject)
def fetch_single_subject(id: int, db: Session = Depends(get_db)):
    return crud.get_subject(db, id=id)
