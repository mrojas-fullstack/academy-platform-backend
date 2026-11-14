from pydantic_settings import BaseSettings, SettingsConfigDict


class GoogleSettings(BaseSettings):
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_REDIRECT_URI: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
