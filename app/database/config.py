from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_NAME: str = "eventilo"
    DATABASE_USER: str = "eventilo"
    DATABASE_PASSWORD: str = "eventilo"
    DATABASE_HOST: str = "db"
    DATABASE_PORT: str = "5432"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()