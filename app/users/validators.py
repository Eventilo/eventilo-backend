from functools import wraps
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from .schemas import CreateUserParams
from .models import User


def validate_user_creation(fn):
    @wraps(fn)
    def wrapper(params: CreateUserParams, db_session: Session, *args, **kwargs):
        username = db_session.scalar(
            select(User).where(User.username == params.username)
        )
        if username:
            raise HTTPException(409, "Username alread taken")
        return fn(params, db_session, *args, **kwargs)

    return wrapper
