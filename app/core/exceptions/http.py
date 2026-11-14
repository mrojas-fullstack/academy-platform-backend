from __future__ import annotations

from typing import cast

from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ConflictException,
    DomainException,
    NotFoundException,
    ValidationException,
)


async def validation_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:

    exception = cast(ValidationException, exc)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "error": "validation_error",
            "message": str(exception),
        },
    )


async def conflict_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:

    exception = cast(ConflictException, exc)

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "conflict_error",
            "message": str(exception),
        },
    )


async def not_found_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:

    exception = cast(NotFoundException, exc)

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "not_found_error",
            "message": str(exception),
        },
    )


async def domain_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:

    exception = cast(DomainException, exc)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "error": "domain_error",
            "message": str(exception),
        },
    )
