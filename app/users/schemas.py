from pydantic import BaseModel, Field


class CreateUserParams(BaseModel):
    username: str = Field(min_length=3, max_length=25)


class UserRepresentation(BaseModel):
    id: int
    username: str
