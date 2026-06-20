import os

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

    assert len(
        data
    ) > 0