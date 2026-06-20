import re


# ######################################
# Knowledge Review Context Service
# ######################################

class KnowledgeReviewContextService:

    def __init__(self):

        self.retrieval_service = (
            None
        )

    # ######################################
    # Get Related Objects
    # ######################################

    def get_related_objects(
        self,
        relationships: list[str]
    ):

        related_objects = []

        for relationship in relationships:

            try:

                related_objects.append(
                    self.retrieval_service
                    .get_object(
                        relationship
                    )
                )

            except Exception:

                pass

        return related_objects

    # ######################################
    # Get Missing Relationships
    # ######################################

    def get_missing_relationships(
        self,
        relationships: list[str]
    ):

        missing_relationships = []

        for relationship in relationships:

            try:

                self.retrieval_service.get_object(
                    relationship
                )

            except Exception:

                missing_relationships.append(
                    relationship
                )

        return missing_relationships

    # ######################################
    # Build Review Context
    # ######################################

    def build_review_context(
        self,
        object_id: str
    ):

        obj = (
            self.retrieval_service
            .get_object(
                object_id
            )
        )

        content = obj.content

        relationships = re.findall(
            r"\[\[([^\]]+)\]\]",
            content
        )

        related_objects = (
            self.get_related_objects(
                relationships
            )
        )

        missing_relationships = (
            self.get_missing_relationships(
                relationships
            )
        )

        return {

            "object_id":
                obj.id,

            "title":
                obj.title,

            "object_type":
                obj.object_type,

            "content":
                content,

            "relationships":
                relationships,

            "related_objects":
                related_objects,

            "missing_relationships":
                missing_relationships
        }