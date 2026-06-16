from app.services.relationship_service import (
    RelationshipService
)


# ######################################
# Test Relationship Lookup
# ######################################

def test_relationship_lookup():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    service = RelationshipService(
        repository_path=repository_path
    )

    result = service.get_related_objects(
        "EID.08"
    )

    assert len(result) > 0

    assert (
        "CNS.005 Knowledge Object Standards"
        in result
    )

    assert (
        "EID.01 Repository Intelligence"
        in result
    )