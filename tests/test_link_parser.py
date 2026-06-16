from app.parsers.link_parser import LinkParser


# ######################################
# Test Link Extraction
# ######################################

def test_extract_links():

    parser = LinkParser()

    content = """
    [[EID.08 Knowledge Intelligence]]

    [[OP.001 Knowledge Intelligence Service]]

    [[CNS.005 Knowledge Object Standards]]
    """

    result = parser.extract_links(
        content
    )

    assert len(result) == 3

    assert (
        "EID.08 Knowledge Intelligence"
        in result
    )

    assert (
        "OP.001 Knowledge Intelligence Service"
        in result
    )

    assert (
        "CNS.005 Knowledge Object Standards"
        in result
    )