from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from projet_plateforme.plateforme_app.database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/forum/users", response_model=schemas.ForumUser)
def create_forum_user(forum_user: schemas.ForumUserCreate, db: Session = Depends(get_db)):
    return crud.create_forum_user(db=db, forum_user=forum_user)

@app.get("/forum/users/{id}", response_model=schemas.ForumUser)
def fetch_forum_user(id: int, db: Session = Depends(get_db)):
    return crud.get_forum_user(db, id=id)