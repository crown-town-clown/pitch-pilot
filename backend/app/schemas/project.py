# project schema 

from pydantic import BaseModel, EmailStr, datetime

class ProjectBase(BaseModel):
    title: str
    description: str
    client_id: int
    status: str
    deadline: datetime
    
class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True