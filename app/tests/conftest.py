from sqlalchemy import create_engine, text
from ..database.config import settings

TEST_DB_NAME = f'{settings.DATABASE_NAME}_TEST'
TEST_DB_URL = "postgresql+psycopg2://{user}:{password}@{host}:{port}".format(
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
)

def create_database():
    engine = create_engine(TEST_DB_URL, isolation_level='AUTOCOMMIT')

    with engine.connect() as connection:
        connection.execute(text(f'DROP DATABASE IF EXISTS {TEST_DB_NAME}'))
        connection.execute(text(f'CREATE DATABASE {TEST_DB_NAME}'))

    engine.dispose()