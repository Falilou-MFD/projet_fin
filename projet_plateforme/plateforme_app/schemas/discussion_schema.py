from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


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
