from unittest.mock import patch

from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(
    app
)


# ######################################
# Repository Write Application Flow
# ######################################

def test_repository_write_application_flow():

    with patch(
        "app.services.github_repository_service.requests.put"
    ) as mock_put:

        mock_response = (
            type(
                "Response",
                (),
                {
                    "raise_for_status":
                        lambda self: None,

                    "json":
                        lambda self: {
                            "commit": {
                                "sha": "123"
                            }
                        }
                }
            )()
        )

        mock_put.return_value = (
            mock_response
        )

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

    assert (
        data["commit"]["sha"]
        == "123"
    )