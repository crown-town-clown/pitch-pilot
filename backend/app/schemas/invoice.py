# invoice schema 

from pydantic import BaseModel, EmailStr, datetime

class InvoiceBase(BaseModel):
    project_id: int
    amount: float
    due_date: datetime
    paid: bool = False
    
class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True