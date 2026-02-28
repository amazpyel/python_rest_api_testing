from typing import Literal

from pydantic import BaseModel, EmailStr

GenderType = Literal["male", "female"]
StatusType = Literal["active", "inactive"]


class UserCreateRequest(BaseModel):
    name: str
    gender: GenderType
    email: EmailStr
    status: StatusType = "active"


class UserUpdateRequest(BaseModel):
    name: str | None = None
    gender: GenderType | None = None
    status: StatusType | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: GenderType
    status: StatusType
