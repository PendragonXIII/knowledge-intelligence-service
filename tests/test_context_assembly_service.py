from app.services.retrieval_service import RetrievalService

from app.services.context_assembly_service import (
    ContextAssemblyService
)


# ######################################
# Test Context Expansion Depth Two
# ######################################

def test_context_expansion_depth_two():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    retrieval_service = RetrievalService(
        repository_path=repository_path
    )

    root_object = retrieval_service.get_object(
        "EID.08"
    )

    assert len(
        root_object.relationships
    ) > 0

    first_related = (
        root_object.relationships[0]
    )

    assert len(
        first_related
    ) > 0


# ######################################
# Test Context Assembly
# ######################################

def test_context_assembly():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    service = ContextAssemblyService(
        repository_path=repository_path
    )

    result = service.build_context(
        "EID.08",
        depth=2
    )

    assert len(result) > 1

    ids = [
        obj.id
        for obj in result
    ]

    assert "EID.08" in ids

    assert "CNS.005" in ids