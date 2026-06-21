import os

from unittest.mock import Mock
from unittest.mock import patch

from app.services.engineering_repository_client import (
    EngineeringRepositoryClient
)


# ######################################
# Client Creation
# ######################################

def test_engineering_repository_client_creation():

    os.environ[
        "ENGINEERING_API_URL"
    ] = (
        "https://test-url"
    )

    os.environ[
        "ENGINEERING_API_KEY"
    ] = (
        "test-key"
    )

    client = (
        EngineeringRepositoryClient()
    )

    assert client is not None

    assert (
        client.base_url
        ==
        "https://test-url"
    )

    assert (
        client.api_key
        ==
        "test-key"
    )

# ######################################
# Search Repository
# ######################################

@patch(
    "app.services.engineering_repository_client.requests.get"
)
def test_search_repository(
    mock_get
):

    mock_response = (
        Mock()
    )

    mock_response.json.return_value = [

        "engineering_endpoints.py"
    ]

    mock_get.return_value = (
        mock_response
    )

    client = (
        EngineeringRepositoryClient()
    )

    result = (
        client.search_repository(
            "repository"
        )
    )

    assert result == [

        "engineering_endpoints.py"
    ]

# ######################################
# Get Document Content
# ######################################

@patch(
    "app.services.engineering_repository_client.requests.get"
)
def test_get_document_content(
    mock_get
):

    mock_response = (
        Mock()
    )

    mock_response.json.return_value = {

        "document":
            "capability_catalog.md",

        "content":
            "Example Content"
    }

    mock_get.return_value = (
        mock_response
    )

    client = (
        EngineeringRepositoryClient()
    )

    result = (
        client.get_document_content(
            "capability_catalog.md"
        )
    )

    assert result[
        "document"
    ] == (
        "capability_catalog.md"
    )

# ######################################
# Get Module Context
# ######################################

@patch(
    "app.services.engineering_repository_client.requests.get"
)
def test_get_module_context(
    mock_get
):

    mock_response = (
        Mock()
    )

    mock_response.json.return_value = {

        "module":
            "repository_reader.py",

        "content":
            "Example",

        "capability":
            "Repository Reader",

        "tests":
            [],

        "dependencies":
            [],

        "dependent_modules":
            []
    }

    mock_get.return_value = (
        mock_response
    )

    client = (
        EngineeringRepositoryClient()
    )

    result = (
        client.get_module_context(
            "repository_reader.py"
        )
    )

    assert result[
        "module"
    ] == (
        "repository_reader.py"
    )

    assert (
        "capability"
        in result
    )