from unittest.mock import Mock

from app.services.repository_write_service import (
    RepositoryWriteService
)


# ######################################
# Create File
# ######################################

def test_create_file():

    service = (
        RepositoryWriteService()
    )

    service.github_service = Mock()

    service.github_service.create_file.return_value = {

        "commit": {

            "sha":
                "123"
        }
    }

    result = (
        service.create_file(
            {
                "path":
                    "Learnings/LRN.999.md",

                "content":
                    "Example"
            }
        )
    )

    assert result[
        "commit"
    ][
        "sha"
    ] == "123"

# ######################################
# Update File
# ######################################

def test_update_file():

    service = (
        RepositoryWriteService()
    )

    result = (
        service.update_file(
            {
                "path":
                    "Capabilities/EID.09.md",

                "content":
                    "Updated"
            }
        )
    )

    assert result == {

        "status":
            "pending",

        "operation":
            "update_file",

        "path":
            "Capabilities/EID.09.md"
    }