import logging
import sys

from app.core.config import settings
from app.core.logging.formatter import AcademyFormatter


def create_logger(
    name: str = "academy"
) -> logging.Logger:

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(
        settings.logging.LOG_LEVEL
    )

    handler = logging.StreamHandler(
        sys.stdout
    )

    handler.setFormatter(
        AcademyFormatter()
    )

    logger.addHandler(handler)

    logger.propagate = False

    return logger


logger = create_logger()