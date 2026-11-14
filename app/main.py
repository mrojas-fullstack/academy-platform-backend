from fastapi import FastAPI

from app.bootstrap import ApplicationBootstrap
from app.core.exceptions import (
    ConflictException,
    DomainException,
    NotFoundException,
    ValidationException,
)
from app.core.exceptions.http import (
    conflict_exception_handler,
    domain_exception_handler,
    not_found_exception_handler,
    validation_exception_handler,
)

app = FastAPI()

app.add_exception_handler(
    ValidationException,
    validation_exception_handler,
)

app.add_exception_handler(
    ConflictException,
    conflict_exception_handler,
)

app.add_exception_handler(
    NotFoundException,
    not_found_exception_handler,
)

app.add_exception_handler(
    DomainException,
    domain_exception_handler,
)

bootstrap = ApplicationBootstrap()

context = bootstrap.build(
    app,
)

app.state.context = context
