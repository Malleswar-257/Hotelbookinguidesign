from pydantic import BaseSettings
class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str
db_settings = Settings()