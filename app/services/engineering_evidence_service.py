from app.services.engineering_repository_client import (
    EngineeringRepositoryClient
)


# ######################################
# Engineering Evidence Service
# ######################################

class EngineeringEvidenceService:

    def __init__(self):

        self.repository_client = (
            EngineeringRepositoryClient()
        )

    # ######################################
    # Build Governance Evidence
    # ######################################

    def build_governance_evidence(
        self
    ):

        capability_catalog = (
            self.repository_client
            .get_document_content(
                "capability_catalog.md"
            )
        )

        capability_matrix = (
            self.repository_client
            .get_document_content(
                "capability_matrix.md"
            )
        )

        architecture = (
            self.repository_client
            .get_document_content(
                "engineering_service_architecture.md"
            )
        )

        return {

            "capability_catalog":
                capability_catalog,

            "capability_matrix":
                capability_matrix,

            "architecture":
                architecture
        }