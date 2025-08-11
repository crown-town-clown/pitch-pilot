# project schema 

from pydantic import BaseModel, EmailStr, date
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "planning"
    deadline: Optional[date] = None
    
class ProjectCreate(ProjectBase):
    client_id: int

class ProjectUpdate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True