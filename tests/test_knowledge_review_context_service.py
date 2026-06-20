from unittest.mock import Mock

from app.services.knowledge_review_context_service import (
    KnowledgeReviewContextService
)

from app.models.knowledge_object import (
    KnowledgeObject
)


# ######################################
# Build Review Context
# ######################################

def test_build_review_context():

    service = (
        KnowledgeReviewContextService()
    )

    service.retrieval_service = (
        Mock()
    )

    def get_object_side_effect(
        object_id
    ):

        if object_id == (
            "EID.08"
        ):

            return KnowledgeObject(

                id="EID.08",

                title="Example",

                object_type="Capability",

                content="""

                [[CNS.005]]

                [[LRN.023]]

                [[OP.999]]

                """
            )

        if object_id == (
            "CNS.005"
        ):

            return KnowledgeObject(

                id="CNS.005",

                title="Constraint",

                object_type="Constraint",

                content="Constraint"
            )

        if object_id == (
            "LRN.023"
        ):

            return KnowledgeObject(

                id="LRN.023",

                title="Learning",

                object_type="Learning",

                content="Learning"
            )

        raise FileNotFoundError()

    service.retrieval_service.get_object.side_effect = (
        get_object_side_effect
    )

    result = (
        service.build_review_context(
            "EID.08"
        )
    )

    assert result[
        "object_id"
    ] == "EID.08"

    assert (
        "relationships"
        in result
    )

    assert (
        "related_objects"
        in result
    )

    assert len(
        result[
            "related_objects"
        ]
    ) == 2

    assert (
        "missing_relationships"
        in result
    )

    assert result[
        "missing_relationships"
    ] == [

        "OP.999"
    ]