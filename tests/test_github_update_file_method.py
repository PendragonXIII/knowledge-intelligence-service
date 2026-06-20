from unittest.mock import Mock
from unittest.mock import patch

from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# Update File
# ######################################

def test_update_file():

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

        "sha":
            "abc123"
    }

    update_response = (
        Mock()
    )

    update_response.raise_for_status.return_value = (
        None
    )

    update_response.json.return_value = {

        "commit": {

            "sha":
                "456"
        }
    }

    with patch(
        "requests.get"
    ) as mock_get:

        with patch(
            "requests.put"
        ) as mock_put:

            mock_get.return_value = (
                metadata_response
            )

            mock_put.return_value = (
                update_response
            )

            result = (
                service.update_file(
                    path=
                        "Capabilities/EID.08.md",

                    content=
                        "Updated",

                    sha=
                        None,

                    message=
                        "Update capability"
                )
            )

    assert result[
        "commit"
    ][
        "sha"
    ] == "456"