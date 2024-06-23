from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from sql import get_db
from user.models import User
from user.password import verify_password
from user.schemas import UserLogin


def authenticate_user(user: UserLogin, db: Session = Depends(get_db)) -> bool:
    """Checks if user with given email exists and if provided password is valid
    """
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()
    if not db_user:
        raise HTTPException(
            status_code=401
        )
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=401
        )
    return True
