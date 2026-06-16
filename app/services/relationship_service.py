from app.services.retrieval_service import RetrievalService


class RelationshipService:

    def __init__(
        self,
        repository_path: str
    ):

        self.retrieval_service = RetrievalService(
            repository_path
        )

    # ######################################
    # Get Related Objects
    # ######################################

    def get_related_objects(
        self,
        object_id: str
    ):

        knowledge_object = (
            self.retrieval_service.get_object(
                object_id
            )
        )

        return knowledge_object.relationships