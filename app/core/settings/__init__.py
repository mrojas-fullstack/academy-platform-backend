from functools import lru_cache

from .app import AppSettings
from .database import DatabaseSettings
from .auth import AuthSettings
from .google import GoogleSettings
from .logging import LoggingSettings


class Settings:

    app: AppSettings
    database: DatabaseSettings
    auth: AuthSettings
    google: GoogleSettings
    logging: LoggingSettings

    def __init__(self) -> None:

        self.app = AppSettings()
        self.database = DatabaseSettings()
        self.auth = AuthSettings()
        self.google = GoogleSettings()
        self.logging = LoggingSettings()


@lru_cache(maxsize=1)
def get_settings() -> Settings:

    return Settings()