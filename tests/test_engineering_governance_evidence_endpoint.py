import os

from unittest.mock import Mock

from fastapi.testclient import (
    TestClient
)

from app.main import (
    app,
    engineering_evidence_service
)

client = (
    TestClient(app)
)


# ######################################
# Governance Evidence Endpoint
# ######################################

def test_governance_evidence_endpoint():

    os.environ[
        "API_KEY"
    ] = "test-key"

    engineering_evidence_service.build_governance_evidence = (
        Mock(
            return_value={

                "capability_catalog":
                    {},

                "capability_matrix":
                    {},

                "architecture":
                    {}
            }
        )
    )

    response = client.get(

        "/engineering/governance-evidence",

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
        "capability_catalog"
        in result
    )

    assert (
        "capability_matrix"
        in result
    )

    assert (
        "architecture"
        in result
    )