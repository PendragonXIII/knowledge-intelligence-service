from unittest.mock import Mock

from app.services.knowledge_comparison_service import (
    KnowledgeComparisonService
)


# ######################################
# Object Exists
# ######################################

def test_object_exists():

    service = (
        KnowledgeComparisonService()
    )

    service.object_resolver = Mock()

    service.object_resolver.resolve_object.return_value = (
        "Capabilities/EID.08.md"
    )

    assert (
        service.object_exists(
            "EID.08"
        )
        is True
    )

# ######################################
# Object Does Not Exist
# ######################################

def test_object_does_not_exist():

    service = (
        KnowledgeComparisonService()
    )

    service.object_resolver = Mock()

    service.object_resolver.resolve_object.side_effect = (
        FileNotFoundError()
    )

    assert (
        service.object_exists(
            "XYZ.999"
        )
        is False
    )

# ######################################
# Compare Candidates
# ######################################

def test_compare_candidates():

    service = (
        KnowledgeComparisonService()
    )

    service.object_resolver = Mock()

    service.object_resolver.resolve_object.side_effect = (
        resolve_side_effect
    )

    result = (
        service.compare_candidates(
            [
                "EID.08",
                "CNS.005",
                "XYZ.999"
            ]
        )
    )

    assert result == {

        "existing": [
            "EID.08",
            "CNS.005"
        ],

        "missing": [
            "XYZ.999"
        ]
    }

def resolve_side_effect(
    object_id
):

    if object_id in [
        "EID.08",
        "CNS.005"
    ]:

        return "exists"

    raise FileNotFoundError()

# ######################################
# Compare Extracted Knowledge
# ######################################

def test_compare_extracted_knowledge():

    service = (
        KnowledgeComparisonService()
    )

    service.object_resolver = Mock()

    service.object_resolver.resolve_object.side_effect = (
        resolve_side_effect
    )

    content = """

    [[CNS.005]]

    [[OP.001]]

    [[LRN.999]]

    """

    result = (
        service.compare_extracted_knowledge(
            content
        )
    )

    assert (
        "constraints"
        in result
    )

    assert (
        "opportunities"
        in result
    )

    assert (
        "learnings"
        in result
    )