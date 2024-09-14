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



class DiscussionCreate(BaseModel):
    id_utilisateur: int
    titre: str
    sous_titre: str
    contenu: str

class Discussion(BaseModel):
    id: int
    id_utilisateur: int
    titre: str
    sous_titre: str
    contenu: str
    creation: datetime

    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ForumUserBase(BaseModel):
    email: str
    mdp: str
    prenom: str
    nom: str
    role: str


class ForumUserCreate(ForumUserBase):
    pass

class ForumUserUpdate(BaseModel):
    email: Optional[str]
    mdp: Optional[str]
    prenom: Optional[str]
    nom: Optional[str]
    role: Optional[str]

# Schema for response
class ForumUser(ForumUserBase):
    id: int
    creation: datetime

    class Config:
        orm_mode = True


from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageBase(BaseModel):
    id_utilisateur: int
    id_discussion: int
    contenu: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    creation: datetime

    class Config:
        orm_mode = True


class ProfileBase(BaseModel):
    num_etu: int
    annee_exp: str
    competences: str
    specialisation: str
    chemin_cv: str

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    creation: datetime

    class Config:
        orm_mode = True


# Schéma pour Student
class StudentBase(BaseModel):
    email: str
    mdp: str
    prenom: str
    nom: str
    dob: str
    niveau: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    num_etu: int
    creation: datetime

    class Config:
        orm_mode = True



class SubjectBase(BaseModel):
    chemin: str
    module: str
    niveau: str
    enseignant: str
    annee_pub: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    creation: datetime

    class Config:
        orm_mode = True


from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str
