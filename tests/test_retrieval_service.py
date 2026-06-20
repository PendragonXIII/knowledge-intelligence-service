from app.services.retrieval_service import RetrievalService


# ######################################
# Test Retrieve Knowledge Object
# ######################################

def test_retrieve_knowledge_object():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    service = RetrievalService(
        repository_path=repository_path
    )

    result = service.get_object(
        "EID.08"
    )

    assert result.id == "EID.08"

    assert (
        "Knowledge Intelligence"
        in result.title
    )

    assert len(
        result.relationships
    ) > 0
    
def test_retrieval_service_has_repository_reader():

    service = RetrievalService(
        repository_path="unused"
    )

    assert (
        service.repository_reader
        is not None
    )

def test_retrieval_service_has_object_resolver():

    service = RetrievalService(
        repository_path="unused"
    )

    assert (
        service.object_resolver
        is not None
    )