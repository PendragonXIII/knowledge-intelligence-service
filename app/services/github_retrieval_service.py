from app.parsers.markdown_parser import (
    MarkdownParser
)

from app.repository.github_repository_reader import (
    GitHubRepositoryReader
)

from app.repository.github_object_resolver import (
    GitHubObjectResolver
)


# ######################################
# GitHub Retrieval Service
# ######################################

class GitHubRetrievalService:

    def __init__(self):

        self.repository_reader = (
            GitHubRepositoryReader()
        )

        self.object_resolver = (
            GitHubObjectResolver()
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
            self.object_resolver
            .resolve_object(
                object_id
            )
        )

        content = (
            self.repository_reader
            .read_file(
                file_path
            )
        )

        filename = (
            file_path.split(
                "/"
            )[-1]
        )

        title = filename.replace(
            f"{object_id} ",
            ""
        ).replace(
            ".md",
            ""
        )

        object_type = (
            file_path.split(
                "/"
            )[0]
        )

        return self.markdown_parser.parse(
            object_id=object_id,
            title=title,
            object_type=object_type,
            content=content
        )