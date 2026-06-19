import os

from fastapi import Header
from fastapi import HTTPException


def verify_api_key(

    x_api_key: str = Header(
        default=None
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