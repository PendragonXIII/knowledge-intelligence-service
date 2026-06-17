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

# ######################################
# Test GitHub Capabilities Endpoint Setup
# ######################################

def test_github_capabilities_endpoint_setup():

    service = (
        GitHubRepositoryService()
    )

    result = service.get_folder_content

    assert result is not None

# ######################################
# Test GitHub Object Endpoint Setup
# ######################################

def test_github_object_endpoint_setup():

    service = (
        GitHubRepositoryService()
    )

    assert (
        service.find_object
        is not None
    )

    assert (
        service.get_file_content
        is not None
    )