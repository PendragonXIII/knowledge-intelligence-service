import pytest

from unittest.mock import Mock
from unittest.mock import patch

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

# ######################################
# Test Get File Content Method Exists
# ######################################

def test_get_file_content_method_exists():

    service = (
        GitHubRepositoryService()
    )

    result = service.get_file_content

    assert result is not None

# ######################################
# Test Find Object Across Repository
# ######################################

def test_find_object_across_repository():

    service = (
        GitHubRepositoryService()
    )

    assert (
        service.find_object
        is not None
    )

# ######################################
# Get File By Path
# ######################################

def test_get_file_by_path():

    service = (
        GitHubRepositoryService()
    )

    metadata_response = (
        Mock()
    )

    metadata_response.raise_for_status.return_value = (
        None
    )

    metadata_response.json.return_value = {

        "download_url":
            "https://example.com/file"
    }

    content_response = (
        Mock()
    )

    content_response.raise_for_status.return_value = (
        None
    )

    content_response.text = (
        "Example Content"
    )

    with patch(
        "requests.get"
    ) as mock_get:

        mock_get.side_effect = [

            metadata_response,
            content_response
        ]

        content = (
            service.get_file_by_path(
                "README.md"
            )
        )

        assert content == (
            "Example Content"
        )

# ######################################
# Get File By Path Repository Override
# ######################################

def test_get_file_by_path_repository_override():

    service = (
        GitHubRepositoryService()
    )

    metadata_response = (
        Mock()
    )

    metadata_response.raise_for_status.return_value = (
        None
    )

    metadata_response.json.return_value = {

        "download_url":
            "https://example.com/file"
    }

    content_response = (
        Mock()
    )

    content_response.raise_for_status.return_value = (
        None
    )

    content_response.text = (
        "Example Content"
    )

    with patch(
        "requests.get"
    ) as mock_get:

        mock_get.side_effect = [

            metadata_response,
            content_response
        ]

        content = (
            service.get_file_by_path(
                path="README.md",
                repository=(
                    "Knowledge-Intelligence-Platform"
                )
            )
        )

        assert content == (
            "Example Content"
        )

# ######################################
# Create File
# ######################################

def test_create_file():

    service = (
        GitHubRepositoryService()
    )

    result = (
        service.create_file(
            path=
                "Learnings/LRN.999.md",

            content=
                "Example",

            message=
                "Create learning"
        )
    )

    assert result == {

        "path":
            "Learnings/LRN.999.md",

        "content":
            "Example",

        "message":
            "Create learning"
    }

# ######################################
# Has GitHub Token
# ######################################

def test_has_github_token():

    service = (
        GitHubRepositoryService()
    )

    result = (
        service.has_github_token()
    )

    assert isinstance(
        result,
        bool
    )