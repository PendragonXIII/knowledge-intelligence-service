from app.services.knowledge_extraction_service import (
    KnowledgeExtractionService
)


# ######################################
# Extract Relationships
# ######################################

def test_extract_relationships():

    service = (
        KnowledgeExtractionService()
    )

    content = """

    [[EID.01]]

    [[EID.02]]

    [[CNS.005]]

    """

    result = (
        service.extract_relationships(
            content
        )
    )

    assert result == [
        "EID.01",
        "EID.02",
        "CNS.005"
    ]

# ######################################
# Extract Capabilities
# ######################################

def test_extract_capabilities():

    service = (
        KnowledgeExtractionService()
    )

    content = """

    ## Capabilities

    - Repository Intelligence
    - Capability Intelligence
    - Knowledge Intelligence

    """

    result = (
        service.extract_capabilities(
            content
        )
    )

    assert result == [
        "Repository Intelligence",
        "Capability Intelligence",
        "Knowledge Intelligence"
    ]

# ######################################
# Extract Constraints
# ######################################

def test_extract_constraints():

    service = (
        KnowledgeExtractionService()
    )

    content = """

    [[EID.08]]

    [[CNS.004]]

    [[CNS.005]]

    [[PLB.003]]

    """

    result = (
        service.extract_constraints(
            content
        )
    )

    assert result == [
        "CNS.004",
        "CNS.005"
    ]

# ######################################
# Extract Opportunities
# ######################################

def test_extract_opportunities():

    service = (
        KnowledgeExtractionService()
    )

    content = """

    [[OP.001]]

    [[OP.002]]

    [[EID.08]]

    [[CNS.005]]

    """

    result = (
        service.extract_opportunities(
            content
        )
    )

    assert result == [
        "OP.001",
        "OP.002"
    ]

# ######################################
# Extract Learnings
# ######################################

def test_extract_learnings():

    service = (
        KnowledgeExtractionService()
    )

    content = """

    [[LRN.001]]

    [[LRN.002]]

    [[EID.08]]

    [[OP.001]]

    """

    result = (
        service.extract_learnings(
            content
        )
    )

    assert result == [
        "LRN.001",
        "LRN.002"
    ]

# ######################################
# Extract Knowledge Candidates
# ######################################

def test_extract_knowledge_candidates():

    service = (
        KnowledgeExtractionService()
    )

    content = """

    [[CNS.005]]

    [[OP.001]]

    [[LRN.001]]

    """

    result = (
        service.extract_knowledge_candidates(
            content
        )
    )

    assert result == {

        "capabilities": [],

        "constraints": [
            "CNS.005"
        ],

        "opportunities": [
            "OP.001"
        ],

        "learnings": [
            "LRN.001"
        ]
    }