import re


# ######################################
# Knowledge Extraction Service
# ######################################

class KnowledgeExtractionService:

    # ######################################
    # Extract Relationships
    # ######################################

    def extract_relationships(
        self,
        content: str
    ):

        return re.findall(
            r"\[\[(.*?)\]\]",
            content
        )
    
    # ######################################
    # Extract Capabilities
    # ######################################

    def extract_capabilities(
        self,
        content: str
    ):

        capabilities = []

        lines = content.splitlines()

        for line in lines:

            line = line.strip()

            if line.startswith(
                "- "
            ):

                capabilities.append(
                    line.replace(
                        "- ",
                        ""
                    ).strip()
                )

        return capabilities
    
    # ######################################
    # Extract Constraints
    # ######################################

    def extract_constraints(
        self,
        content: str
    ):

        constraints = []

        relationships = (
            self.extract_relationships(
                content
            )
        )

        for relationship in relationships:

            if relationship.startswith(
                "CNS."
            ):

                constraints.append(
                    relationship
                )

        return constraints
    
    # ######################################
    # Extract Opportunities
    # ######################################

    def extract_opportunities(
        self,
        content: str
    ):

        opportunities = []

        relationships = (
            self.extract_relationships(
                content
            )
        )

        for relationship in relationships:

            if relationship.startswith(
                "OP."
            ):

                opportunities.append(
                    relationship
                )

        return opportunities
    
    # ######################################
    # Extract Learnings
    # ######################################

    def extract_learnings(
        self,
        content: str
    ):

        learnings = []

        relationships = (
            self.extract_relationships(
                content
            )
        )

        for relationship in relationships:

            if relationship.startswith(
                "LRN."
            ):

                learnings.append(
                    relationship
                )

        return learnings
    
    # ######################################
    # Extract Knowledge Candidates
    # ######################################

    def extract_knowledge_candidates(
        self,
        content: str
    ):

        return {

            "capabilities":
                self.extract_capabilities(
                    content
                ),

            "constraints":
                self.extract_constraints(
                    content
                ),

            "opportunities":
                self.extract_opportunities(
                    content
                ),

            "learnings":
                self.extract_learnings(
                    content
                )
        }