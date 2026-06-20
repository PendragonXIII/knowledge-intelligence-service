from app.services.knowledge_maintenance_service import (
    KnowledgeMaintenanceService
)


# ######################################
# Generate Recommendations
# ######################################

def test_generate_recommendations():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_recommendations(
            {
                "existing": [
                    "CNS.005"
                ],

                "missing": [
                    "LRN.999"
                ]
            }
        )
    )

    assert result == [

        {
            "action":
                "ignore",

            "object_id":
                "CNS.005"
        },

        {
            "action":
                "create",

            "object_id":
                "LRN.999"
        }
    ]

# ######################################
# Generate Maintenance Plan
# ######################################

def test_generate_maintenance_plan():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_maintenance_plan(
            [
                {
                    "action":
                        "create",

                    "object_id":
                        "LRN.999"
                }
            ]
        )
    )

    assert result == [

        {
            "action":
                "create",

            "object_id":
                "LRN.999",

            "folder":
                "Learnings"
        }
    ]

# ######################################
# Generate File Template
# ######################################

def test_generate_file_template():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_file_template(
            "LRN.999"
        )
    )

    assert (
        "## Purpose"
        in result
    )

    assert (
        "## Current State"
        in result
    )

# ######################################
# Generate Maintenance Actions
# ######################################

def test_generate_maintenance_actions():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_maintenance_actions(
            {
                "existing": [
                    "EID.08"
                ],

                "missing": [
                    "LRN.999"
                ]
            }
        )
    )

    assert result == [

        {
            "action":
                "update",

            "object_id":
                "EID.08"
        },

        {
            "action":
                "create",

            "object_id":
                "LRN.999"
        }
    ]

# ######################################
# Generate Update Plan
# ######################################

def test_generate_update_plan():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_update_plan(
            object_id="EID.08",
            change_type="relationship"
        )
    )

    assert result == {

        "object_id":
            "EID.08",

        "action":
            "add_relationship"
    }

# ######################################
# Add Relationship
# ######################################

def test_add_relationship():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.add_relationship(
            [
                "EID.01",
                "EID.02"
            ],
            "EID.03"
        )
    )

    assert result == [
        "EID.01",
        "EID.02",
        "EID.03"
    ]

# ######################################
# Add Relationship Duplicate
# ######################################

def test_add_relationship_duplicate():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.add_relationship(
            [
                "EID.01",
                "EID.02"
            ],
            "EID.02"
        )
    )

    assert result == [
        "EID.01",
        "EID.02"
    ]

# ######################################
# Append Bullet
# ######################################

def test_append_bullet():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.append_bullet(
            [
                "- Existing Item"
            ],
            "New Item"
        )
    )

    assert result == [
        "- Existing Item",
        "- New Item"
    ]

# ######################################
# Append Bullet Duplicate
# ######################################

def test_append_bullet_duplicate():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.append_bullet(
            [
                "- Existing Item"
            ],
            "Existing Item"
        )
    )

    assert result == [
        "- Existing Item"
    ]

# ######################################
# Append Section
# ######################################

def test_append_section():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.append_section(
            "## Existing Section",
            "## New Section"
        )
    )

    assert (
        "## New Section"
        in result
    )

# ######################################
# Append Section Duplicate
# ######################################

def test_append_section_duplicate():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.append_section(
            "## Existing Section",
            "## Existing Section"
        )
    )

    assert (
        result
        ==
        "## Existing Section"
    )

# ######################################
# Replace Section
# ######################################

def test_replace_section():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.replace_section(
            content="""
## Outcomes

Old Content
""",
            old_section="""
## Outcomes

Old Content
""",
            new_section="""
## Outcomes

New Content
"""
        )
    )

    assert (
        "New Content"
        in result
    )

    assert (
        "Old Content"
        not in result
    )

# ######################################
# Replace Section Not Found
# ######################################

def test_replace_section_not_found():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.replace_section(
            content="ABC",
            old_section="XYZ",
            new_section="NEW"
        )
    )

    assert (
        result
        == "ABC"
    )

# ######################################
# Rewrite Content
# ######################################

def test_rewrite_content():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.rewrite_content(
            """
New Content
"""
        )
    )

    assert (
        result
        ==
        """
New Content
"""
    )

# ######################################
# Generate Repository Modification
# ######################################

def test_generate_repository_modification():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_repository_modification(
            {
                "action":
                    "create",

                "object_id":
                    "LRN.999"
            }
        )
    )

    assert result == {

        "operation":
            "create_file",

        "path":
            "Learnings/LRN.999.md"
    }

# ######################################
# Create File Modification
# ######################################

def test_create_file_modification():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.create_file_modification(
            "LRN.999"
        )
    )

    assert (
        result[
            "path"
        ]
        ==
        "Learnings/LRN.999.md"
    )

    assert (
        "## Purpose"
        in
        result[
            "content"
        ]
    )

# ######################################
# Generate Write Request
# ######################################

def test_generate_write_request():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_write_request(
            repository=
                "Garden Knowledge",

            modification={
                "path":
                    "Learnings/LRN.999.md",

                "content":
                    "Example"
            }
        )
    )

    assert result == {

        "repository":
            "Garden Knowledge",

        "path":
            "Learnings/LRN.999.md",

        "content":
            "Example"
    }

# ######################################
# Generate File Update Request
# ######################################

def test_generate_file_update_request():

    service = (
        KnowledgeMaintenanceService()
    )

    result = (
        service.generate_file_update_request(
            path=
                "Capabilities/EID.09.md",

            content=
                "Updated"
        )
    )

    assert result == {

        "operation":
            "update_file",

        "path":
            "Capabilities/EID.09.md",

        "content":
            "Updated"
    }