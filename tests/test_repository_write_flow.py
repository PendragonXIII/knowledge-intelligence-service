from unittest.mock import Mock

from app.services.knowledge_maintenance_service import (
    KnowledgeMaintenanceService
)

from app.services.repository_write_service import (
    RepositoryWriteService
)


# ######################################
# Write Flow
# ######################################

def test_write_flow():

    maintenance_service = (
        KnowledgeMaintenanceService()
    )

    write_service = (
        RepositoryWriteService()
    )

    write_service.github_service = (
        Mock()
    )

    write_service.github_service.create_file.return_value = {

        "commit": {

            "sha":
                "123"
        }
    }

    request = (
        maintenance_service
        .generate_write_request(
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

    result = (
        write_service.create_file(
            request
        )
    )

    assert result[
        "commit"
    ][
        "sha"
    ] == "123"