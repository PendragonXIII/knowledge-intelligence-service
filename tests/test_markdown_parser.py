from app.parsers.markdown_parser import MarkdownParser


# ######################################
# Test Parse Knowledge Object
# ######################################

def test_parse_knowledge_object():

    parser = MarkdownParser()

    content = """
    ## Related

    [[EID.08 Knowledge Intelligence]]

    [[CNS.005 Knowledge Object Standards]]
    """

    result = parser.parse(
        object_id="TEST.001",
        title="Test Object",
        object_type="Test",
        content=content
    )

    assert result.id == "TEST.001"

    assert result.title == "Test Object"

    assert result.object_type == "Test"

    assert len(result.relationships) == 2

    assert (
        "EID.08 Knowledge Intelligence"
        in result.relationships
    )

    assert (
        "CNS.005 Knowledge Object Standards"
        in result.relationships
    )