from sqlalchemy.orm import Session
from .. import models, schemas
from passlib.hash import bcrypt
import uuid

# Récupérer un administrateur par email
def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()

# Récupérer un administrateur par son ID
def get_admin(db: Session, admin_id: str):
    return db.query(models.Admin).filter(models.Admin.num_admin == admin_id).first()

# Récupérer tous les administrateurs
def get_admins(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Admin).offset(skip).limit(limit).all()

# Créer un nouvel administrateur
def create_admin(db: Session, admin: schemas.AdminCreate):
    hashed_password = bcrypt.hash(admin.mdp)
    db_admin = models.Admin(
        num_admin="A" + str(uuid.uuid4()),  # Génération d'un identifiant unique
        email=admin.email,
        mdp=hashed_password,
        prenom=admin.prenom,
        nom=admin.nom,
        poste=admin.poste
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

# Mettre à jour un administrateur
def update_admin(db: Session, db_admin: models.Admin, admin_update: schemas.AdminCreate):
    db_admin.email = admin_update.email
    db_admin.prenom = admin_update.prenom
    db_admin.nom = admin_update.nom
    db_admin.poste = admin_update.poste
    if admin_update.mdp:
        db_admin.mdp = bcrypt.hash(admin_update.mdp)
    db.commit()
    db.refresh(db_admin)
    return db_admin

# Supprimer un administrateur
def delete_admin(db: Session, db_admin: models.Admin):
    db.delete(db_admin)
    db.commit()
    return db_admin
