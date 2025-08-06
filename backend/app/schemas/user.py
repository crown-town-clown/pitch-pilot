# user schema 

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    password: str
    role: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True