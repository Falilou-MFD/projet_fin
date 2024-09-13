from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

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
