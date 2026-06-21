from unittest.mock import Mock

from app.services.engineering_code_evidence_service import (
    EngineeringCodeEvidenceService
)


def test_get_module_context():

    service = (
        EngineeringCodeEvidenceService()
    )

    service.repository_client = (
        Mock()
    )

    service.repository_client.get_module_context.return_value = {

        "module":
            "repository_reader.py"
    }

    result = (
        service.get_module_context(
            "repository_reader.py"
        )
    )

    assert result[
        "module"
    ] == (
        "repository_reader.py"
    )

# ######################################
# Search Repository
# ######################################

def test_search_repository():

    service = (
        EngineeringCodeEvidenceService()
    )

    service.repository_client = (
        Mock()
    )

    service.repository_client.search_repository.return_value = [

        "engineering_repository_client.py"
    ]

    result = (
        service.search_repository(
            "repository"
        )
    )

    assert result == [

        "engineering_repository_client.py"
    ]

# ######################################
# Get Repository File
# ######################################

def test_get_repository_file():

    service = (
        EngineeringCodeEvidenceService()
    )

    service.repository_client = (
        Mock()
    )

    service.repository_client.get_repository_file.return_value = {

        "content":
            "class RepositoryReader"
    }

    result = (
        service.get_repository_file(
            "repository_reader.py"
        )
    )

    assert (
        "content"
        in result
    )

    assert (
        "RepositoryReader"
        in result[
            "content"
        ]
    )