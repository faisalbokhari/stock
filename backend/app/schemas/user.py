
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.user 
