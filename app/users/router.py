from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .schemas import CreateUserParams, UserRepresentation
from .models import User
from ..database.dependencies import get_db_session
from .services import create_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/", response_model=UserRepresentation, status_code=status.HTTP_201_CREATED
)

def create(user: User = Depends(create_user)):
    return user