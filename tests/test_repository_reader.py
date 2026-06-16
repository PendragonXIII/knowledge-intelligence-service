from app.repository.repository_reader import RepositoryReader


# ######################################
# Test Read File
# ######################################

def test_read_file():

    repository_path = (
        r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
    )

    reader = RepositoryReader(
        repository_path=repository_path
    )

    result = reader.read_file(
        "Capabilities\\EID.08 Knowledge Intelligence.md"
    )

    assert len(result) > 0

    assert (
        "Knowledge Intelligence"
        in result
    )