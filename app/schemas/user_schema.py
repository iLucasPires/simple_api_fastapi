from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str

    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserShow(BaseModel):
    username: str
    email: str


class UserInDB(BaseModel):
    id: int
    created_at: str
    updated_at: str


class UserLogin(BaseModel):
    username: str
    password: str
