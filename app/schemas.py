from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional

# Validates user registration input
class UserCreate(BaseModel):
    username: str
    password: str
# Controls what user data is returned (hides password)
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
# Defines the JWT token structure
class Token(BaseModel):
    access_token: str
    token_type: str
# Stores decoded token info
class TokenData(BaseModel):
    username: str | None = None

class JobCreate(BaseModel):
    company: str
    position: str
    status: str = "Applied"

class JobResponse(JobCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class JobUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    status: Optional[str] = None

