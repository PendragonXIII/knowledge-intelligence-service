import os

from unittest.mock import Mock
from unittest.mock import patch

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

    with patch(
        "app.main.repository_content_service"
    ) as mock_service:
        
        mock_service.get_repository_file.return_value = (
            "Example README"
        )   

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