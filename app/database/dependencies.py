from sqlalchemy.orm import sessionmaker
from .connection import engine


def get_db_session():
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = session_local()
    try:
        yield db_session
    finally:
        db_session.close()
