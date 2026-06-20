from unittest.mock import Mock

from app.services.reference_validation_service import (
    ReferenceValidationService
)


# ######################################
# Validate Relationships
# ######################################

def test_validate_relationships():

    service = (
        ReferenceValidationService()
    )

    service.object_resolver = (
        Mock()
    )

    def resolve_side_effect(
        object_id
    ):

        if object_id in [

            "EID.08",
            "CNS.005"
        ]:

            return "exists"

        raise FileNotFoundError()

    service.object_resolver.resolve_object.side_effect = (
        resolve_side_effect
    )

    result = (
        service.validate_relationships(
            [

                "EID.08",
                "CNS.005",
                "OP.999"
            ]
        )
    )

    assert result == {

        "existing": [

            "EID.08",
            "CNS.005"
        ],

        "missing": [

            "OP.999"
        ]
    }

# ######################################
# Validate Object Content
# ######################################

def test_validate_object_content():

    service = (
        ReferenceValidationService()
    )

    service.object_resolver = (
        Mock()
    )

    def resolve_side_effect(
        object_id
    ):

        if object_id in [

            "EID.08",
            "CNS.005"
        ]:

            return "exists"

        raise FileNotFoundError()

    service.object_resolver.resolve_object.side_effect = (
        resolve_side_effect
    )

    content = """

    [[EID.08]]

    [[CNS.005]]

    [[OP.999]]

    """

    result = (
        service.validate_object_content(
            content
        )
    )

    assert result == {

        "existing": [

            "EID.08",
            "CNS.005"
        ],

        "missing": [

            "OP.999"
        ]
    }