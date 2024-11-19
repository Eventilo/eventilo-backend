from fastapi import HTTPException


class UsernameAlreadyExists(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=409, detail="Username already exists.")
