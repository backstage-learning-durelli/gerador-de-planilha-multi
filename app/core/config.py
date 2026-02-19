"""Application configuration settings."""
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "gerador-de-planilha-multi"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
