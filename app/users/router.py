from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .schemas import CreateUserParams, UserRepresentation
from .models import User
from ..database.dependencies import get_db_session

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/", response_model=UserRepresentation, status_code=status.HTTP_201_CREATED
)
def create_user(
    user_params: CreateUserParams, db_session: Session = Depends(get_db_session)
):
    user = User(username=user_params.username)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
