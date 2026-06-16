from pathlib import Path

from app.parsers.markdown_parser import MarkdownParser
from app.repository.object_resolver import ObjectResolver
from app.repository.repository_reader import RepositoryReader


class RetrievalService:

    def __init__(self, repository_path: str):

        self.repository_reader = RepositoryReader(
            repository_path
        )

        self.object_resolver = ObjectResolver(
            repository_path
        )

        self.markdown_parser = MarkdownParser()

    # ######################################
    # Get Object
    # ######################################

    def get_object(
        self,
        object_id: str
    ):

        file_path = self.object_resolver.resolve_object(
            object_id
        )

        content = self.repository_reader.read_file(
            file_path.name
        )

        title = file_path.stem.replace(
            f"{object_id} ",
            ""
        )

        object_type = file_path.parent.name

        return self.markdown_parser.parse(
            object_id=object_id,
            title=title,
            object_type=object_type,
            content=content
        )