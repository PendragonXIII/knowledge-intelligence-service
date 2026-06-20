from unittest.mock import Mock

from app.services.repository_content_service import (
    RepositoryContentService
)


# ######################################
# Get Repository File
# ######################################

def test_get_repository_file():

    service = (
        RepositoryContentService()
    )

    service.github_service = Mock()

    service.github_service.get_file_by_path.return_value = (
        "Example README"
    )

    content = (
        service.get_repository_file(
            repository=(
                "Knowledge-Intelligence-Platform"
            ),
            path="README.md"
        )
    )

    assert content == (
        "Example README"
    )

    assert len(
        content
    ) > 0

# ######################################
# Get Repository Folder
# ######################################

def test_get_repository_folder():

    service = (
        RepositoryContentService()
    )

    service.github_service = Mock()

    service.github_service.get_folder_content.return_value = [
        {
            "name":
                "EID.08 Repository Retrieval Intelligence.md"
        }
    ]

    result = (
        service.get_repository_folder(
            "Capabilities"
        )
    )

    assert result is not None

    assert len(
        result
    ) == 1