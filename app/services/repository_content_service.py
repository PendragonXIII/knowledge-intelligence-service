from app.services.github_repository_service import (
    GitHubRepositoryService
)


# ######################################
# Repository Content Service
# ######################################

class RepositoryContentService:

    def __init__(self):

        self.github_service = (
            GitHubRepositoryService()
        )

    # ######################################
    # Get Repository File
    # ######################################

    def get_repository_file(
        self,
        repository: str,
        path: str
    ):

        return (
            self.github_service
            .get_file_by_path(
                path=path,
                repository=repository
            )
        )
    
    # ######################################
    # Get Repository Folder
    # ######################################

    def get_repository_folder(
        self,
        folder_name: str
    ):

        return (
            self.github_service
            .get_folder_content(
                folder_name
            )
        )