from datetime import datetime

from sqlalchemy import UUID, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy_utils import create_database, database_exists

from main import get_settings

engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
)
if not database_exists(engine.url):
    create_database(engine.url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    """Base model provdes base fields that every model shuld have
    """
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        sort_order=-3
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        sort_order=-2
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        sort_order=-1
    )
