from unittest.mock import patch

from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(
    app
)


# ######################################
# Create Endpoint
# ######################################

def test_create_repository_file():

    with patch(
        "app.main.repository_write_service"
    ) as mock_service:

        mock_service.create_file.return_value = {

            "commit": {

                "sha":
                    "123"
            }
        }

        response = client.post(
            "/repository/write/create",
            json={
                "path":
                    "Learnings/LRN.999.md",

                "content":
                    "Example"
            }
        )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert data[
        "commit"
    ][
        "sha"
    ] == "123"


# ######################################
# Update Endpoint
# ######################################

def test_update_repository_file():

    with patch(
        "app.main.repository_write_service"
    ) as mock_service:

        mock_service.update_file.return_value = {

            "commit": {

                "sha":
                    "456"
            }
        }

        response = client.post(
            "/repository/write/update",

            json={

                "path":
                    "Capabilities/EID.09.md",

                "content":
                    "Updated"
            }
        )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert data[
        "commit"
    ][
        "sha"
    ] == "456"