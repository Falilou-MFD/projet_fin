
from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.forum_user_model import ForumUser
from projet_plateforme.plateforme_app.schemas.forum_user_schema import ForumUserCreate
from projet_plateforme.plateforme_app.auth import get_password_hash

def create_forum_user(db: Session, forum_user: schemas.ForumUserCreate):
    hashed_password = get_password_hash(forum_user.password)  # Hacher le mot de passe
    db_forum_user = models.ForumUser(
        username=forum_user.username,
        hashed_password=hashed_password  # Enregistrer le mot de passe haché
    )
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
