
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

# UserRole Enum remains the same
class UserRole(str, Enum):
    admin = "admin"
    user = "user"

# UserBase remains the same
class UserBase(BaseModel):
    username: str
    email: EmailStr

# NEW SCHEMA: UserCreatePublic - Removes the 'role' field to prevent privilege escalation
class UserCreatePublic(UserBase):
    password: str

# UserCreate is now used only for internal/admin purposes if needed, 
# but the public registration should use UserCreatePublic
class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.user

# UserOut remains the same
class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
