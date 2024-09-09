from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DiscussionBase(BaseModel):
    title: str
    content: str

class DiscussionCreate(DiscussionBase):
    pass

class Discussion(DiscussionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True