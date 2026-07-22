import logging


class AcademyFormatter(logging.Formatter):

    def __init__(self) -> None:

        super().__init__(
            fmt=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(name)s | "
                "%(module)s:%(lineno)d | "
                "%(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S",
        )