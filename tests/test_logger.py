from app.core.logging import logger


def test_logger():

    logger.info(
        "Logger working"
    )

    assert logger.name == "academy"