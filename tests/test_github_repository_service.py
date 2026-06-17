from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# Test GitHub Repository Service
# ######################################

def test_github_repository_service_creation():

    service = (
        GitHubRepositoryService()
    )

    assert service.owner == (
        "PendragonXIII"
    )

    assert service.repository == (
        "Knowledge-Intelligence-Platform"
    )