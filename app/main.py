# ######################################
# Imnports
# ######################################

from fastapi import FastAPI

from app.services.retrieval_service import RetrievalService

from app.services.github_retrieval_service import (
    GitHubRetrievalService
)

from app.services.context_assembly_service import (
    ContextAssemblyService
)

from app.services.github_repository_service import (
    GitHubRepositoryService
)

from fastapi import Depends

from app.auth import (
    verify_api_key
)

from app.services.repository_content_service import (
    RepositoryContentService
)

from app.services.repository_write_service import (
    RepositoryWriteService
)

from app.models.repository_write_request import (
    RepositoryWriteRequest
)

from app.services.knowledge_review_context_service import (
    KnowledgeReviewContextService
)

from app.services.engineering_evidence_service import (
    EngineeringEvidenceService
)

from app.services.engineering_repository_client import (
    EngineeringRepositoryClient
)

from app.services.engineering_code_evidence_service import (
    EngineeringCodeEvidenceService
)

app = FastAPI(
    title="Knowledge Intelligence Service",
    version="0.1.0",
    servers=[
        {
            "url": "https://knowledge-intelligence-service-production.up.railway.app"
        }
    ]
)

# ######################################
# Service-Initialisierungen
# ######################################

repository_path = (
    r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
)

retrieval_service = RetrievalService(
    repository_path=repository_path
)

github_retrieval_service = (
    GitHubRetrievalService()
)

context_service = ContextAssemblyService(
    repository_path=repository_path
)

github_repository_service = (
    GitHubRepositoryService()
)

repository_content_service = (
    RepositoryContentService()
)

repository_write_service = (
    RepositoryWriteService()
)

review_context_service = (
    KnowledgeReviewContextService()
)

review_context_service.retrieval_service = (
    github_retrieval_service
)

engineering_evidence_service = (
    EngineeringEvidenceService()
)

engineering_evidence_service.repository_client = (
    EngineeringRepositoryClient()
)

engineering_code_evidence_service = (
    EngineeringCodeEvidenceService()
)

engineering_code_evidence_service.repository_client = (
    EngineeringRepositoryClient()
)


# ######################################
# Health Check
# ######################################

@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "knowledge-intelligence-service",
        "deployment_test": "AUTH_DEBUG_V1"
    }


# ######################################
# Get Knowledge Object
# ######################################

@app.get("/objects/{object_id}")
def get_object(
    object_id: str,
    auth = Depends(
        verify_api_key
    )
):

    return retrieval_service.get_object(
        object_id
    )

# ######################################
# Get Context Pack
# ######################################

@app.get("/context/{object_id}")
def get_context(
    object_id: str,
    _: None = Depends(
        verify_api_key
    )
):

    return context_service.build_context(
        object_id=object_id,
        depth=2
    )

# ######################################
# GitHub Repository Test
# ######################################

@app.get("/github-test")
def github_test():

    return (
        github_repository_service
        .get_root_content()
    )

# ######################################
# GitHub Capabilities Test
# ######################################

@app.get("/github-test/capabilities")
def github_capabilities_test():

    return (
        github_repository_service
        .get_folder_content(
            "Capabilities"
        )
    )

# ######################################
# GitHub Object Test
# ######################################

@app.get(
    "/github-test/object/{object_id}"
)
def github_object_test(
    object_id: str
):

    path = (
        github_repository_service
        .find_object(
            object_id
        )
    )

    content = (
        github_repository_service
        .get_file_content(
            path
        )
    )

    return {
        "path": path,
        "preview": content[:200]
    }

# ######################################
# Repository File
# ######################################

@app.get("/repository/file")
def get_repository_file(
    path: str,
    _: None = Depends(
        verify_api_key
    )
):

    return {
        "content":
            repository_content_service
            .get_repository_file(
                repository=repository,
                path=path
            )
    }

# ######################################
# Repository Folder
# ######################################

@app.get("/repository/folder")
def get_repository_folder(
    folder_name: str,
    _: None = Depends(
        verify_api_key
    )
):

    return (
        repository_content_service
        .get_repository_folder(
            folder_name
        )
    )

# ######################################
# Review Context
# ######################################

@app.get(
    "/review-context/{object_id}"
)
def get_review_context(
    object_id: str,
    _: None = Depends(
        verify_api_key
    )
):

    return (
        review_context_service
        .build_review_context(
            object_id
        )
    )

# ######################################
# Repository Write Create
# ######################################

@app.post(
    "/repository/write/create"
)
def create_repository_file(
    request: RepositoryWriteRequest
):

    return (
        repository_write_service.create_file(
            request.model_dump()
        )
    )

# ######################################
# Repository Write Update
# ######################################

@app.post(
    "/repository/write/update"
)
def update_repository_file(
    request: RepositoryWriteRequest
):

    return (
        repository_write_service.update_file(
            request.model_dump()
        )
    )

# ######################################
# Engineering Governance Evidence
# ######################################

@app.get(
    "/engineering/governance-evidence"
)
def get_governance_evidence(
    _: None = Depends(
        verify_api_key
    )
):

    return (
        engineering_evidence_service
        .build_governance_evidence()
    )

# ######################################
# Engineering Module Context
# ######################################

@app.get(
    "/engineering/module-context"
)
def get_engineering_module_context(

    module_name: str,

    _: None = Depends(
        verify_api_key
    )
):

    return (
        engineering_code_evidence_service
        .get_module_context(
            module_name
        )
    )