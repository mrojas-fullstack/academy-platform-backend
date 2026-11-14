from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
