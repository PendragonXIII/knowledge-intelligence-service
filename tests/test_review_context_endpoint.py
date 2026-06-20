import os

from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(
    app
)


# ######################################
# Review Context Endpoint
# ######################################

def test_review_context_endpoint():

    os.environ[
        "API_KEY"
    ] = "test-key"

    response = client.get(
        "/review-context/EID.08",
        headers={
            "x-api-key":
                "test-key"
        }
    )

    assert (
        response.status_code
        == 200
    )