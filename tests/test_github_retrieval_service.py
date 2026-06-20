from unittest.mock import Mock

from app.services.github_retrieval_service import (
    GitHubRetrievalService
)


# ######################################
# Service Creation
# ######################################

def test_github_retrieval_service_creation():

    service = (
        GitHubRetrievalService()
    )

    assert service is not None

    assert (
        service.repository_reader
        is not None
    )

    assert (
        service.object_resolver
        is not None
    )

# ######################################
# Get Object
# ######################################

def test_get_object():

    service = (
        GitHubRetrievalService()
    )

    service.object_resolver = (
        Mock()
    )

    service.repository_reader = (
        Mock()
    )

    service.object_resolver.resolve_object.return_value = (
        "Capabilities/EID.08 Example.md"
    )

    service.repository_reader.read_file.return_value = (
        "# Example"
    )

    result = (
        service.get_object(
            "EID.08"
        )
    )

    assert result.id == (
        "EID.08"
    )