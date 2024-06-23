from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from settings import get_settings

engine = create_engine(
    get_settings().db_url
)
if not database_exists(engine.url):
    create_database(engine.url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Returns DB object to use
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
