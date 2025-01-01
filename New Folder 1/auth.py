# Authentication endpoints
from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from ..models import User
from ..schemas.user import UserCreate, UserResponse
from ..database.session import get_db

""" 
Initializing Router, creating user, 
hashing password, adding user to db
and returning UserResponse
"""

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def create_user(user_data: UserCreate, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    hashed_psw = bcrypt.hash(user_data.hashed_password)

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        hashed_password=hashed_psw,
        created_at=datetime.now(),
        updated_at=None
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        id=new_user.id,
        name=new_user.name,
        email=new_user.email,
        role=new_user.role,
        created_at=new_user.created_at,
        updated_at=new_user.updated_at
    )
