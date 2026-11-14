from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str

    DATABASE_ECHO: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
