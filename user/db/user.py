from sqlalchemy.orm import Session

from user.models import User
from user.utils.password import hash_password
from user.schemas import UserCreate


def insert_user(db: Session, user: UserCreate) -> User:
    """Inserts User into DB
    """
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        password=hashed_password,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
