# proposal schema 

from pydantic import BaseModel, EmailStr
from typing import Optional

class ProposalBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_ai_generated: Optional[bool] = True
    
class ProposalCreate(ProposalBase):
    project_id: int

class ProposalUpdate(ProposalBase):
    pass

class Proposal(ProposalBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True

# AI endpoints
class NotesIn(BaseModel):
    notes: str

class GeneratedTextOut(BaseModel):
    text: str