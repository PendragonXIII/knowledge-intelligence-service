from unittest.mock import Mock

from app.services.engineering_evidence_service import (
    EngineeringEvidenceService
)


# ######################################
# Service Creation
# ######################################

def test_engineering_evidence_service_creation():

    service = (
        EngineeringEvidenceService()
    )

    assert service is not None

    assert (
        service.repository_client
        is not None
    )

# ######################################
# Build Governance Evidence
# ######################################

def test_build_governance_evidence():

    service = (
        EngineeringEvidenceService()
    )

    service.repository_client = (
        Mock()
    )

    service.repository_client.get_document_content.side_effect = [

        {
            "document":
                "capability_catalog.md"
        },

        {
            "document":
                "capability_matrix.md"
        },

        {
            "document":
                "engineering_service_architecture.md"
        }
    ]

    result = (
        service.build_governance_evidence()
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