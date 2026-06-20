import os

from unittest.mock import patch

from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(
    app
)


# ######################################
# Repository Folder Endpoint
# ######################################

def test_repository_folder_endpoint():

    os.environ[
        "API_KEY"
    ] = "test-key"

    with patch(
        "app.main.repository_content_service"
    ) as mock_service:

        mock_service.get_repository_folder.return_value = [
            {
                "name":
                    "EID.08 Repository Retrieval Intelligence.md"
            }
        ]

        response = client.get(
            "/repository/folder",
            params={
                "folder_name":
                    "Capabilities"
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

    assert len(data) == 1

    assert (
        data[0]["name"]
        == "EID.08 Repository Retrieval Intelligence.md"
    )