from fastapi import Depends
from sqlalchemy.orm import Session

from sql import get_db
from user.models import User
from user.schemas import UserLogin
from user.utils.password import verify_password


def authenticate_user(user: UserLogin, db: Session = Depends(get_db)) -> User | bool:
    """Checks if user with given email exists and if provided password is valid
    """
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()
    if not db_user:
        return False
    if not verify_password(user.password, db_user.password):
        return False
    return db_user
