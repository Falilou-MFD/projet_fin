from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


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
