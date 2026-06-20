import os

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(
    app
)


# ######################################
# Repository File Endpoint
# ######################################

def test_repository_file_endpoint():

    os.environ[
        "API_KEY"
    ] = "test-key"

    response = client.get(
        "/repository/file",
        params={
            "repository":
                "Knowledge-Intelligence-Platform",
            "path":
                "README.md"
        },
        headers={
            "x-api-key":
                "test-key"
        }
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert "content" in data