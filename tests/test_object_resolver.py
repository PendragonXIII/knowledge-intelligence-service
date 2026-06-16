from app.repository.object_resolver import ObjectResolver


# ######################################
# Test Object Resolution
# ######################################

def test_resolve_object():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    resolver = ObjectResolver(
        repository_path=repository_path
    )

    result = resolver.resolve_object(
        "EID.08"
    )

    assert result.exists()

    assert (
        "EID.08 Knowledge Intelligence.md"
        in str(result)
    )