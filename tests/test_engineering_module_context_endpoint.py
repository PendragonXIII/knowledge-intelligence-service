import os

from unittest.mock import Mock

from fastapi.testclient import (
    TestClient
)

from app.main import (
    app,
    engineering_code_evidence_service
)

client = (
    TestClient(app)
)


def test_engineering_module_context_endpoint():

    os.environ[
        "API_KEY"
    ] = "test-key"

    engineering_code_evidence_service.get_module_context = (
        Mock(
            return_value={
                "module":
                    "repository_reader.py"
            }
        )
    )

    response = client.get(

        "/engineering/module-context",

        params={
            "module_name":
                "repository_reader.py"
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

    result = (
        response.json()
    )

    assert (
        result["module"]
        ==
        "repository_reader.py"
    )