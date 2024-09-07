from sqlalchemy.orm import Session
from models.forum_user_model import ForumUser
from schemas.forum_user_schema import ForumUserCreate

def create_forum_user(db: Session, forum_user: ForumUserCreate):
    db_forum_user = ForumUser(**forum_user.dict())
    db.add(db_forum_user)
    db.commit()
    db.refresh(db_forum_user)
    return db_forum_user

def get_forum_user_by_id(db: Session, user_id: int):
    return db.query(ForumUser).filter(ForumUser.id == user_id).first()

def get_all_forum_users(db: Session):
    return db.query(ForumUser).all()

def update_forum_user(db: Session, user_id: int, updated_forum_user: ForumUserCreate):
    forum_user = get_forum_user_by_id(db, user_id)
    if forum_user:
        for key, value in updated_forum_user.dict().items():
            setattr(forum_user, key, value)
        db.commit()
        db.refresh(forum_user)
    return forum_user

def delete_forum_user(db: Session, user_id: int):
    forum_user = get_forum_user_by_id(db, user_id)
    if forum_user:
        db.delete(forum_user)
        db.commit()
    return forum_user
