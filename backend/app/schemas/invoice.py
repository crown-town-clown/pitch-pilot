# invoice schema 

from pydantic import BaseModel, EmailStr, date
from typing import Optional

class InvoiceBase(BaseModel):
    amount: float
    due_date: Optional[date] = None
    paid: Optional[bool] = False
    description: Optional[str] = None
    
class InvoiceCreate(InvoiceBase):
    project_id: int

class InvoiceUpdate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True