from .schemas import CreateUserParams
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from ..database.dependencies import get_db_session
from .models import User
from sqlalchemy import select


def create_user(
    params: CreateUserParams, db_session: Session = Depends(get_db_session)
):
    username = db_session.scalar(
        select(User).where(User.username == params.username)
    )  # zawara piewsze rekord lub null
    if username:
        raise HTTPException(409, "Username alread taken")

    user = User(**params.model_dump())
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

    # try:
    #     user = User(**params.model_dump())
    # except:
    #     pass
    # else:
    #     db_session.add(user)
    #     db_session.commit()
    #     db_session.refresh(user)
    #     return user
