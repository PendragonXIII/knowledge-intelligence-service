from pathlib import Path

from app.parsers.markdown_parser import MarkdownParser
from app.repository.object_resolver import ObjectResolver
from app.repository.repository_reader import RepositoryReader
from app.services.github_repository_service import (
    GitHubRepositoryService
)


class RetrievalService:

    def __init__(self, repository_path: str):

        self.github_repository_service = (
            GitHubRepositoryService()
        )

        self.markdown_parser = (
            MarkdownParser()
        )

    # ######################################
    # Get Object
    # ######################################

    def get_object(
        self,
        object_id: str
    ):

        file_path = (
            self.github_repository_service
            .find_object(
                object_id
            )
        )

        content = (
            self.github_repository_service
            .get_file_content(
                file_path
            )
        )

        filename = (
            file_path
            .split("/")[-1]
        )

        title = filename.replace(
            f"{object_id} ",
            ""
        ).replace(
            ".md",
            ""
        )

        object_type = (
            file_path
            .split("/")[0]
        )

        return self.markdown_parser.parse(
            object_id=object_id,
            title=title,
            object_type=object_type,
            content=content
        )