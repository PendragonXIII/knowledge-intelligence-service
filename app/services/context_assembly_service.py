from app.services.retrieval_service import RetrievalService


class ContextAssemblyService:

    def __init__(
        self,
        repository_path: str
    ):

        self.retrieval_service = RetrievalService(
            repository_path
        )

    # ######################################
    # Build Context
    # ######################################

    def build_context(
        self,
        object_id: str,
        depth: int = 2
    ):

        visited = set()

        return self._collect_context(
            object_id=object_id,
            depth=depth,
            visited=visited
        )

    # ######################################
    # Collect Context
    # ######################################

    def _collect_context(
        self,
        object_id: str,
        depth: int,
        visited: set
    ):

        if depth < 0:
            return []

        if object_id in visited:
            return []

        visited.add(
            object_id
        )

        knowledge_object = (
            self.retrieval_service.get_object(
                object_id
            )
        )

        context = [
            knowledge_object
        ]

        for relationship in (
            knowledge_object.relationships
        ):

            related_id = (
                relationship.split(" ")[0]
            )

            try:

                context.extend(
                    self._collect_context(
                        object_id=related_id,
                        depth=depth - 1,
                        visited=visited
                    )
                )

            except Exception:
                pass

        return context