
from sqlalchemy.orm import Session
from models.profile_model import Profile
from schemas.profile_schema import ProfileCreate

from sqlalchemy.orm import Session
from .. import models, schemas

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def get_profiles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Profile).offset(skip).limit(limit).all()

def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile_id: int, profile: schemas.ProfileCreate):
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if db_profile:
        for key, value in profile.dict().items():
            setattr(db_profile, key, value)
        db.commit()
        db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, profile_id: int):
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if db_profile:
        db.delete(db_profile)
        db.commit()
    return db_profile
