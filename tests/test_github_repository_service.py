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

# ######################################
# Test Folder Content Method Exists
# ######################################

def test_folder_content_method_exists():

    service = (
        GitHubRepositoryService()
    )

    result = service.get_folder_content

    assert result is not None

# ######################################
# Test Find Object Method Exists
# ######################################

def test_find_object_method_exists():

    service = (
        GitHubRepositoryService()
    )

    result = service.find_object

    assert result is not None