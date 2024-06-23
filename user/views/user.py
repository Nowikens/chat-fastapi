import re

from fastapi import Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from sql import get_db
from user.auth import authenticate_user
from user.db import insert_user
from user.models import User as UserModel
from user.routers import router
from user.schemas import UserCreate, UserLogin, UserResponse


def validate_password(password: str) -> bool:
    """Cheks if password is strong enough
    """
    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long"
        )
    if not re.search(r"[A-Z]", password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter"
        )
    if not re.search(r"[a-z]", password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one lowercase letter"
        )
    if not re.search(r"[0-9]", password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one digit"
        )
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one special character"
        )
    return True


def validate_new_user(user: UserCreate, db: Session = Depends(get_db)) -> bool:
    """Validates new user's data.
    """
    db_user = db.query(UserModel).filter(
        or_(
            UserModel.username == user.username,
            UserModel.email == user.email
        )
    ).first()
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="username or email taken"
        )
    return validate_password(user.password)


@router.post("/user/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """View responsible for creating users
    """
    validate_new_user(user=user, db=db)
    return insert_user(db=db, user=user)


@router.post("/login/", response_model=bool)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """User login
    """
    return authenticate_user(user, db)
