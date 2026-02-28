from pydantic import BaseModel, EmailStr


class UserCreateRequest(BaseModel):
    name: str
    gender: str
    email: EmailStr
    status: str = "active"


class UserUpdateRequest(BaseModel):
    name: str | None = None
    gender: str | None = None
    status: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: str
    status: str
