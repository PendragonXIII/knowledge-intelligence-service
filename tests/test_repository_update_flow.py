from unittest.mock import Mock

from app.services.knowledge_maintenance_service import (
    KnowledgeMaintenanceService
)

from app.services.repository_write_service import (
    RepositoryWriteService
)


# ######################################
# Update Flow
# ######################################

def test_update_flow():

    maintenance_service = (
        KnowledgeMaintenanceService()
    )

    write_service = (
        RepositoryWriteService()
    )

    write_service.github_service = (
        Mock()
    )

    write_service.github_service.update_file.return_value = {

        "commit": {

            "sha":
                "456"
        }
    }

    request = (
        maintenance_service
        .generate_write_request(
            repository=
                "Garden Knowledge",

            modification={

                "path":
                    "Capabilities/EID.09.md",

                "content":
                    "Updated"
            }
        )
    )

    result = (
        write_service.update_file(
            request
        )
    )

    assert result[
        "commit"
    ][
        "sha"
    ] == "456"