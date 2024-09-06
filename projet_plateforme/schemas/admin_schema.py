from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AdminBase(BaseModel):
    num_admin: str
    name: str
    email: str

class AdminCreate(AdminBase):
    pass

class Admin(AdminBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
