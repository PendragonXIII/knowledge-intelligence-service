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

    content = (
        service.get_repository_file(
            repository=(
                "Knowledge-Intelligence-Platform"
            ),
            path="README.md"
        )
    )

    assert content is not None

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

    result = (
        service.get_repository_folder(
            "Capabilities"
        )
    )

    assert result is not None

    assert len(
        result
    ) > 0