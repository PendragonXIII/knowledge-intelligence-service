from app.services.github_configuration_service import (
    GitHubConfigurationService
)


# ######################################
# Service Exists
# ######################################

def test_service_exists():

    service = (
        GitHubConfigurationService()
    )

    assert (
        service
        is not None
    )


# ######################################
# Has GitHub Token
# ######################################

def test_has_github_token():

    service = (
        GitHubConfigurationService()
    )

    result = (
        service.has_github_token()
    )

    assert isinstance(
        result,
        bool
    )