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

    assert result == {

        "path":
            "Learnings/LRN.999.md",

        "content":
            "Example",

        "message":
            "Create file"
    }

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