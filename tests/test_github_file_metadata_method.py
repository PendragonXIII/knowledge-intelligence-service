from unittest.mock import Mock
from unittest.mock import patch

from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# Get File Metadata
# ######################################

def test_get_file_metadata():

    service = (
        GitHubRepositoryService()
    )

    mock_response = (
        Mock()
    )

    mock_response.raise_for_status.return_value = (
        None
    )

    mock_response.json.return_value = {

        "sha":
            "abc123",

        "path":
            "Capabilities/EID.08.md"
    }

    with patch(
        "requests.get"
    ) as mock_get:

        mock_get.return_value = (
            mock_response
        )

        result = (
            service.get_file_metadata(
                "Capabilities/EID.08.md"
            )
        )

    assert result["sha"] == (
        "abc123"
    )