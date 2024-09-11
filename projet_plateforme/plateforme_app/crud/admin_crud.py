from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.admin_model import Admin
from projet_plateforme.plateforme_app.schemas.admin_schema import AdminCreate
from projet_plateforme.plateforme_app.auth import get_password_hash

def create_admin(db: Session, admin: AdminCreate):
    hashed_password = get_password_hash(admin.password)  # Hacher le mot de passe
    db_admin = models.Admin(
        num_admin=admin.num_admin,
        name=admin.name,
        email=admin.email,
        hashed_password=hashed_password  # Enregistrer le mot de passe haché
        )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_admin_by_num(db: Session, num_admin: str):
    return db.query(Admin).filter(Admin.num_admin == num_admin).first()

def get_all_admins(db: Session):
    return db.query(Admin).all()

def update_admin(db: Session, num_admin: str, updated_admin: AdminCreate):
    admin = get_admin_by_num(db, num_admin)
    if admin:
        for key, value in updated_admin.dict().items():
            setattr(admin, key, value)
        db.commit()
        db.refresh(admin)
    return admin

def delete_admin(db: Session, num_admin: str):
    admin = get_admin_by_num(db, num_admin)
    if admin:
        db.delete(admin)
        db.commit()
    return admin
