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
