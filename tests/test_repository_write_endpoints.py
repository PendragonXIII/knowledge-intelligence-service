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


# ######################################
# Update Endpoint
# ######################################

def test_update_repository_file():

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