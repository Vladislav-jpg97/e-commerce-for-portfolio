from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.models.mixins import LanguageEnum

PROJECT_ROOT = Path(__file__).resolve().parents[4]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        case_sensitive=False,
        extra="ignore"
    )
    database_url: str

    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int
    jwt_refresh_token_expire_days: int

    default_language: LanguageEnum

settings = Settings()
