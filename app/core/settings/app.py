from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):

    APP_NAME: str = "Academy Platform"

    APP_VERSION: str = "1.0.0"

    APP_ENV: str = "development"

    APP_DEBUG: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )