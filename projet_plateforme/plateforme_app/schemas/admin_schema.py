from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Schéma de base pour l'Admin (les champs communs)
class AdminBase(BaseModel):
    email: str
    prenom: str
    nom: str
    poste: str

# Schéma pour la création d'un Admin (inclut le mot de passe)
class AdminCreate(AdminBase):
    mdp: str  # Mot de passe en texte clair à hacher
    email: str
    prenom: str
    nom: str
    poste: str

# Schéma de retour avec tous les champs
class Admin(AdminBase):
    num_admin: str
    creation: datetime

    class Config:
        from_attributes = True


# from pydantic import BaseModel

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: str | None = None

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str
