from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from sql import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
        comment="Email is used as login"
    )
    password: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Hashed password"
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="User's username to be used in chat"
    )
