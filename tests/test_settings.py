from app.core.config import get_settings


def test_singleton_settings():

    settings1 = get_settings()

    settings2 = get_settings()

    assert settings1 is settings2
