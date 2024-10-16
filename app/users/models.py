from app.database.model import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
