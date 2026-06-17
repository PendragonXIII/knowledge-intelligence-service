from app.auth import verify_api_key


def test_verify_api_key_exists():

    assert verify_api_key is not None