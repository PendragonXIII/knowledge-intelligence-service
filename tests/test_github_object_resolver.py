from unittest.mock import Mock

from app.repository.github_object_resolver import (
    GitHubObjectResolver
)


# ######################################
# Resolve Object
# ######################################

def test_resolve_object():

    resolver = (
        GitHubObjectResolver()
    )

    resolver.github_service = (
        Mock()
    )

    resolver.github_service.find_object.return_value = (
        "Capabilities/EID.08 Example.md"
    )

    result = (
        resolver.resolve_object(
            "EID.08"
        )
    )

    assert result == (
        "Capabilities/EID.08 Example.md"
    )