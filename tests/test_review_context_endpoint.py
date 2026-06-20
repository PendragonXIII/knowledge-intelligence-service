import os

from unittest.mock import Mock

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

    from app.main import (
    review_context_service
)

    review_context_service.build_review_context = (
        Mock(
            return_value={
                "object_id":
                    "EID.08",

                "content":
                    "Example",

                "relationships":
                    [],

                "related_objects":
                    [],

                "missing_relationships":
                    []
            }
        )
    )

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