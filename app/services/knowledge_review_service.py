from app.services.knowledge_review_context_service import (
    KnowledgeReviewContextService
)


# ######################################
# Knowledge Review Service
# ######################################

class KnowledgeReviewService:

    def __init__(self):

        self.context_service = (
            KnowledgeReviewContextService()
        )

    # ######################################
    # Build Review Prompt
    # ######################################

    def build_review_prompt(
        self,
        review_context: dict
    ):

                return f"""

You are a Knowledge Governance Reviewer.

Your responsibility is to review knowledge objects and identify
maintenance opportunities within the knowledge repository.

Review the following object.

Object ID:
{review_context["object_id"]}

Content:
{review_context["content"]}

Relationships:
{review_context["relationships"]}

Related Objects:
{review_context["related_objects"]}

Missing Relationships:
{review_context["missing_relationships"]}

Perform the following review:

1. Identify referenced objects that appear to be missing.

2. Identify relationships that may be missing.

3. Identify governance gaps, such as:
   - missing constraints
   - missing learnings
   - missing opportunities
   - missing capability references

4. Identify inconsistencies between the object and its related objects.

5. Recommend maintenance actions.

Return findings using the following structure:

CRITICAL:
- ...

HIGH:
- ...

MEDIUM:
- ...

LOW:
- ...

RECOMMENDED ACTIONS:
- ...

"""

    # ######################################
    # Review Object
    # ######################################

    def review_object(
        self,
        object_id: str
    ):

        review_context = (
            self.context_service
            .build_review_context(
                object_id
            )
        )

        review_prompt = (
            self.build_review_prompt(
                review_context
            )
        )

        return {

            "object_id":
                object_id,

            "review_context":
                review_context,

            "review_prompt":
                review_prompt
        }