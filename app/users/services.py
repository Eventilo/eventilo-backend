from .schemas import CreateUserParams
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database.dependencies import get_db_session
from .models import User
from .validators import validate_user_creation


@validate_user_creation
def create_user(
    params: CreateUserParams, db_session: Session = Depends(get_db_session)
):
    user = User(**params.model_dump())
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
