from app.services.github_repository_service import (
    GitHubRepositoryService
)

# ######################################
# Repository Write Service
# ######################################

class RepositoryWriteService:

    def __init__(
        self
    ):

        self.github_service = (
            GitHubRepositoryService()
        )

    # ######################################
    # Create File
    # ######################################

    def create_file(
        self,
        request: dict
    ):

        return (
            self.github_service.create_file(
                path=request[
                    "path"
                ],

                content=request[
                    "content"
                ],

                message=(
                    "Create file"
                )
            )
        )
    
    # ######################################
    # Update File
    # ######################################

    def update_file(
        self,
        request: dict
    ):

        return {

            "status":
                "pending",

            "operation":
                "update_file",

            "path":
                request[
                    "path"
                ]
        }