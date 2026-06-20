from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# GitHub Repository Reader
# ######################################

class GitHubRepositoryReader:

    def __init__(self):

        self.github_service = (
            GitHubRepositoryService()
        )

    # ######################################
    # Read File
    # ######################################

    def read_file(
        self,
        path: str
    ):

        return (
            self.github_service
            .get_file_by_path(
                path
            )
        )