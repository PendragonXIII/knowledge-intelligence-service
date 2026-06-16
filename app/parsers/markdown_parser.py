from app.models.knowledge_object import KnowledgeObject
from app.parsers.link_parser import LinkParser


class MarkdownParser:

    def __init__(self):
        self.link_parser = LinkParser()

    # ######################################
    # Parse Knowledge Object
    # ######################################

    def parse(
        self,
        object_id: str,
        title: str,
        object_type: str,
        content: str
    ) -> KnowledgeObject:

        relationships = self.link_parser.extract_links(
            content
        )

        return KnowledgeObject(
            id=object_id,
            title=title,
            object_type=object_type,
            content=content,
            relationships=relationships
        )