from unittest.mock import Mock

from app.repository.github_repository_reader import (
    GitHubRepositoryReader
)


# ######################################
# Reader Creation
# ######################################

def test_github_repository_reader_creation():

    reader = (
        GitHubRepositoryReader()
    )

    assert reader is not None

    assert (
        reader.github_service
        is not None
    )

# ######################################
# Read File
# ######################################

def test_read_file():

    reader = (
        GitHubRepositoryReader()
    )

    reader.github_service = (
        Mock()
    )

    reader.github_service.get_file_by_path.return_value = (
        "Example Content"
    )

    result = (
        reader.read_file(
            "Capabilities/EID.08.md"
        )
    )

    assert result == (
        "Example Content"
    )