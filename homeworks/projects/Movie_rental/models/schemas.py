from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int = Optional[int]
    username: str = Field(..., min_length=2, max_length=20)
    password: str = Field(..., min_length=6, max_length=100)
    email: str = Field(..., min_length=5, max_length=50)


class Movie(BaseModel):
    title: str = Field(..., min_length=2, max_length=30)
    genre: str = Field(..., min_length=2, max_length=30)
    rating: float = Field(..., gt=0.09)


class Rental(BaseModel):
    user: User
    movie: str = Field(..., min_length=2, max_length=30)
    rental_duration: float = Field(..., gt=0.0, lt=10)

