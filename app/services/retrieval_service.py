from pathlib import Path

from app.parsers.markdown_parser import MarkdownParser
from app.repository.object_resolver import ObjectResolver
from app.repository.repository_reader import RepositoryReader


class RetrievalService:

    def __init__(self, repository_path: str):

        self.repository_reader = (
            RepositoryReader(
                repository_path
            )
        )

        self.object_resolver = (
            ObjectResolver(
                repository_path
            )
        )

        self.markdown_parser = (
            MarkdownParser()
        )

        self.object_resolver = (
            ObjectResolver(
                repository_path
            )
        )

    # ######################################
    # Get Object
    # ######################################

    def get_object(
        self,
        object_id: str
    ):

        file_path = (
            self.object_resolver
            .resolve_object(
                object_id
            )
        )

        content = (
            self.repository_reader
            .read_file(
                str(
                    file_path.relative_to(
                        self.repository_reader
                        .repository_path
                    )
                )
            )
        )

        filename = (
            file_path.name
        )

        title = filename.replace(
            f"{object_id} ",
            ""
        ).replace(
            ".md",
            ""
        )

        object_type = (
            file_path.parts[0]
        )

        return self.markdown_parser.parse(
            object_id=object_id,
            title=title,
            object_type=object_type,
            content=content
        )