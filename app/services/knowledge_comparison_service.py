from app.services.github_repository_service import (
    GitHubRepositoryService
)

from app.services.knowledge_extraction_service import (
    KnowledgeExtractionService
)


# ######################################
# Knowledge Comparison Service
# ######################################

class KnowledgeComparisonService:

    def __init__(self):

        self.github_service = (
            GitHubRepositoryService()
        )

        self.extraction_service = (
            KnowledgeExtractionService()
        )

    # ######################################
    # Object Exists
    # ######################################

    def object_exists(
        self,
        object_id: str
    ):

        try:

            self.github_service.find_object(
                object_id
            )

            return True

        except FileNotFoundError:

            return False
        
    # ######################################
    # Compare Candidates
    # ######################################

    def compare_candidates(
        self,
        candidates: list[str]
    ):

        result = {

            "existing": [],

            "missing": []
        }

        for candidate in candidates:

            if self.object_exists(
                candidate
            ):

                result[
                    "existing"
                ].append(
                    candidate
                )

            else:

                result[
                    "missing"
                ].append(
                    candidate
                )

        return result
    
    # ######################################
    # Compare Extracted Knowledge
    # ######################################

    def compare_extracted_knowledge(
        self,
        content: str
    ):

        candidates = (
            self.extraction_service
            .extract_knowledge_candidates(
                content
            )
        )

        return {

            "constraints":
                self.compare_candidates(
                    candidates[
                        "constraints"
                    ]
                ),

            "opportunities":
                self.compare_candidates(
                    candidates[
                        "opportunities"
                    ]
                ),

            "learnings":
                self.compare_candidates(
                    candidates[
                        "learnings"
                    ]
                )
        }