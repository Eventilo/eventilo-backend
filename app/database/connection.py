from sqlalchemy import create_engine
from .config import settings

DATABASE_URL = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}".format(
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,  # nazwa service z docker compose yml
    port=settings.DATABASE_PORT,
    name=settings.DATABASE_NAME,
)

engine = create_engine(DATABASE_URL)
