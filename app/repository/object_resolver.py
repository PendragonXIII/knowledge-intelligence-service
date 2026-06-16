from pathlib import Path


class ObjectResolver:

    def __init__(self, repository_path: str):
        self.repository_path = Path(repository_path)

    # ######################################
    # Resolve Object
    # ######################################

    def resolve_object(
        self,
        object_id: str
    ) -> Path:

        matches = list(
            self.repository_path.rglob(
                f"{object_id}*.md"
            )
        )

        if not matches:
            raise FileNotFoundError(
                f"Knowledge Object not found: {object_id}"
            )

        return matches[0]