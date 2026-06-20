from unittest.mock import Mock
from unittest.mock import patch

from app.services.github_repository_service import (
    GitHubRepositoryService
)


def test_create_file():

    service = (
        GitHubRepositoryService()
    )

    mock_response = Mock()

    mock_response.json.return_value = {

        "commit": {

            "sha":
                "123"
        }
    }

    with patch(
        "requests.put"
    ) as mock_put:

        mock_put.return_value = (
            mock_response
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

    assert result[
        "commit"
    ][
        "sha"
    ] == "123"