from functools import wraps
from sqlalchemy.orm import Session
from sqlalchemy import select
from .schemas import CreateUserParams
from .models import User
from .exceptions import UsernameAlreadyExists


def validate_user_creation(fn):
    @wraps(fn)
    def wrapper(params: CreateUserParams, db_session: Session, *args, **kwargs):
        username = db_session.scalar(
            select(User).where(User.username == params.username)
        )
        if username:
            raise UsernameAlreadyExists()
        return fn(params, db_session, *args, **kwargs)

    return wrapper
