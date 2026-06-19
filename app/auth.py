from fastapi import HTTPException


def verify_api_key():

    raise HTTPException(
        status_code=401,
        detail="AUTH TEST"
    )