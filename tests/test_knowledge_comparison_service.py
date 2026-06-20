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

# ######################################
# Compare Extracted Knowledge
# ######################################

def test_compare_extracted_knowledge():

    service = (
        KnowledgeComparisonService()
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