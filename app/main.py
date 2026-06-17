from fastapi import FastAPI

from app.services.retrieval_service import RetrievalService
from app.services.context_assembly_service import (
    ContextAssemblyService
)

from app.services.github_repository_service import (
    GitHubRepositoryService
)

app = FastAPI(
    title="Knowledge Intelligence Service",
    version="0.1.0"
)


repository_path = (
    r"C:\Users\tkulg\OneDrive\AI Projects\Garden Knowledge"
)

retrieval_service = RetrievalService(
    repository_path=repository_path
)

context_service = ContextAssemblyService(
    repository_path=repository_path
)

github_repository_service = (
    GitHubRepositoryService()
)


# ######################################
# Health Check
# ######################################

@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "knowledge-intelligence-service"
    }


# ######################################
# Get Knowledge Object
# ######################################

@app.get("/objects/{object_id}")
def get_object(
    object_id: str
):

    return retrieval_service.get_object(
        object_id
    )

# ######################################
# Get Context Pack
# ######################################

@app.get("/context/{object_id}")
def get_context(
    object_id: str
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