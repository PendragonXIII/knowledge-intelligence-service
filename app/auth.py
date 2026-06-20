import os

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import APIKeyHeader


api_key_header = APIKeyHeader(
    name="x-api-key",
    auto_error=False
)


def verify_api_key(

    x_api_key: str | None = Depends(
        api_key_header
    )

):

    expected_key = os.getenv(
        "API_KEY"
    )

    if x_api_key != expected_key:

        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )