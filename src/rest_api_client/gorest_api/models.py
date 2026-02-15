from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreateRequest(BaseModel):
    name: str
    gender: str
    email: EmailStr
    status: str = "active"

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    status: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: str
    status: str
