from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# Pydantic model for creating a new membership


class MembershipCreate(BaseModel):
    type: str
    expired_day: date
    remaining_books: int

# Pydantic model for updating an existing membership


class MembershipUpdate(BaseModel):
    type: Optional[str] = None
    expired_day: Optional[date] = None
    remaining_books: Optional[int] = None

# Pydantic model for membership response


class MembershipResponse(BaseModel):
    user_id: int
    type: str
    expired_day: date
    remaining_books: int
