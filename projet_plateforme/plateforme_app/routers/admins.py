from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db
from typing import List

app = APIRouter()

# Créer un nouvel administrateur
@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    return crud.create_admin(db, admin)

# Récupérer tous les administrateurs
@app.get("/admins/", response_model=List[schemas.Admin])
def read_admins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    admins = crud.get_admins(db, skip=skip, limit=limit)
    return admins

# Récupérer un administrateur par son ID
@app.get("/admins/{admin_id}", response_model=schemas.Admin)
def read_admin(admin_id: str, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Administrateur non trouvé")
    return db_admin

# Mettre à jour un administrateur
@app.put("/admins/{admin_id}", response_model=schemas.Admin)
def update_admin(admin_id: str, admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Administrateur non trouvé")
    return crud.update_admin(db, db_admin, admin)

# Supprimer un administrateur
@app.delete("/admins/{admin_id}", response_model=schemas.Admin)
def delete_admin(admin_id: str, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Administrateur non trouvé")
    return crud.delete_admin(db, db_admin)
