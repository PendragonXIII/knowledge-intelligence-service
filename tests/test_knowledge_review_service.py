from unittest.mock import Mock

from app.services.knowledge_review_service import (
    KnowledgeReviewService
)


# ######################################
# Review Object
# ######################################

def test_review_object():

    service = (
        KnowledgeReviewService()
    )

    service.context_service = (
        Mock()
    )

    service.context_service.build_review_context.return_value = {

        "object_id":
            "EID.08",

        "content":
            "Example Content",

        "relationships":
            [
                "CNS.005"
            ],

        "related_objects":
            [],

        "missing_relationships":
            [
                "OP.999"
            ]
    }

    result = (
        service.review_object(
            "EID.08"
        )
    )

    assert result[
        "object_id"
    ] == "EID.08"

    assert (
        "review_prompt"
        in result
    )

    assert (
        "Knowledge Governance Reviewer"
        in result[
            "review_prompt"
        ]
    )

    assert (
        "CRITICAL:"
        in result[
            "review_prompt"
        ]
    )

    assert (
        "RECOMMENDED ACTIONS:"
        in result[
            "review_prompt"
        ]
    )

    assert (
        "missing constraints"
        in result[
            "review_prompt"
        ]
    )

    assert (
        "Missing Relationships:"
        in result[
            "review_prompt"
        ]
    )