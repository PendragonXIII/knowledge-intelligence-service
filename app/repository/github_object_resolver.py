from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# GitHub Object Resolver
# ######################################

class GitHubObjectResolver:

    def __init__(self):

        self.github_service = (
            GitHubRepositoryService()
        )

    # ######################################
    # Resolve Object
    # ######################################

    def resolve_object(
        self,
        object_id: str
    ):

        return (
            self.github_service
            .find_object(
                object_id
            )
        )