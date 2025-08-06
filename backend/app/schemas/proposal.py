# proposal schema 

from pydantic import BaseModel, EmailStr, 

class ProposalBase(BaseModel):
    title: str
    content: str
    project_id: int
    is_ai_generated: bool = True
    
class ProposalCreate(ProposalBase):
    pass

class Proposal(ProposalBase):
    id: int

    class Config:
        orm_mode = True
    