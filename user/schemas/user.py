from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    username: str


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str
