from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# Test GitHub Endpoint Dependencies
# ######################################

def test_github_repository_service_exists():

    service = (
        GitHubRepositoryService()
    )

    assert service is not None