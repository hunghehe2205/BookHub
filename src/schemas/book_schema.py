from pydantic import BaseModel
from typing import Optional
from datetime import date

# Pydantic model for book creation request
class BookCreate(BaseModel):
    title: str
    author: str
    publication_date: date
    rating: float = 0
    release_date: date

# Pydantic model for book update request
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_date: Optional[date] = None
    rating: Optional[float] = None
    release_date: Optional[date] = None

# Pydantic model for book response
class BookResponse(BaseModel):
    book_id: int
    title: str
    author: str
    publication_date: date
    rating: float
    release_date: date
