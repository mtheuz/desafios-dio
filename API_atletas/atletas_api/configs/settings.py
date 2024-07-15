from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Define the settings here
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:abacaxi01@localhost/workout')
    
settings = Settings()