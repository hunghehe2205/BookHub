from pydantic import BaseModel, EmailStr

# Pydantic model for user registration request


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Pydantic model for user update request


class UserUpdate(BaseModel):
    username: str = None
    email: EmailStr = None
    password: str = None
    streak: int = None


# Pydantic model for user response
class UserResponse(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    streak: int
