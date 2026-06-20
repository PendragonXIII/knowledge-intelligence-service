from app.repository.object_resolver import (
    ObjectResolver
)


# ######################################
# Knowledge Consistency Service
# ######################################

class ReferenceValidationService:

    def __init__(
        self,
        repository_path: str = (
            "Garden Knowledge"
        )
    ):

        self.object_resolver = (
            ObjectResolver(
                repository_path
            )
        )

    # ######################################
    # Validate Relationships
    # ######################################

    def validate_relationships(
        self,
        object_ids: list[str]
    ):

        result = {

            "existing": [],

            "missing": []
        }

        for object_id in object_ids:

            try:

                self.object_resolver.resolve_object(
                    object_id
                )

                result[
                    "existing"
                ].append(
                    object_id
                )

            except (
                FileNotFoundError,
                ValueError
            ):

                result[
                    "missing"
                ].append(
                    object_id
                )

        return result
    
    # ######################################
    # Validate Object Content
    # ######################################

    def validate_object_content(
        self,
        content: str
    ):

        import re

        object_ids = re.findall(
            r"\[\[([^\]]+)\]\]",
            content
        )

        return (
            self.validate_relationships(
                object_ids
            )
        )