from app.services.retrieval_service import RetrievalService


# ######################################
# Test Related Objects
# ######################################

def test_related_objects():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    service = RetrievalService(
        repository_path=repository_path
    )

    result = service.get_object(
        "EID.08"
    )

    assert (
        "CNS.005 Knowledge Object Standards"
        in result.relationships
    )

    assert (
        "EID.01 Repository Intelligence"
        in result.relationships
    )