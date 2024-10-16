from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}".format(
    user="eventilo",
    password="eventilo",
    host="db",  # nazwa service z docker compose yml
    port=5432,
    name="eventilo",
)

engine = create_engine(DATABASE_URL)
