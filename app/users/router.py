from fastapi import APIRouter, Depends, status
from .schemas import UserRepresentation
from .models import User
from .services import create_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/", response_model=UserRepresentation, status_code=status.HTTP_201_CREATED
)
def create(user: User = Depends(create_user)):
    return user
