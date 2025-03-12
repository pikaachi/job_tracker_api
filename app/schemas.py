from pydantic import BaseModel
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
