from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.forum_user_model import *
from ..crud.forum_user_crud import *
from ..database import SessionLocal, engine
from .. import crud_def as crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from .. import crud_def as crud
from ..schemas import forum_user_schema
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db



@app.post("/forum/users", response_model=ForumUser)
def create_forum_user(user: ForumUserCreate, db: Session = Depends(get_db)):
    return crud.create_forum_user(db=db, user=user)

@app.get("/forum/users/{user_id}", response_model=ForumUser)
def get_forum_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_forum_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/forum/users/{user_id}", response_model=ForumUser)
def update_forum_user(user_id: int, user: ForumUserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_forum_user(db, user_id=user_id, user=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/forum/users/{user_id}", response_model=ForumUser)
def delete_forum_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_forum_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
