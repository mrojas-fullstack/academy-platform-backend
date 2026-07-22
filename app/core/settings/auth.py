from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):

    JWT_SECRET: str

    JWT_ALGORITHM: str = "HS256"

    JWT_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )