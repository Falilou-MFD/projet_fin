
from sqlalchemy.orm import Session
from ..models.forum_user_model import ForumUser
from ..schemas.forum_user_schema import ForumUserCreate, ForumUserUpdate
from ..auth import get_password_hash
from .. import schemas, models

def create_forum_user(db: Session, user: ForumUserCreate):
    db_user = ForumUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_forum_user_by_id(db: Session, user_id: int):
    return db.query(ForumUser).filter(ForumUser.id == user_id).first()

def update_forum_user(db: Session, user_id: int, user: ForumUserUpdate):
    db_user = get_forum_user_by_id(db, user_id=user_id)
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_forum_user(db: Session, user_id: int):
    db_user = get_forum_user_by_id(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
