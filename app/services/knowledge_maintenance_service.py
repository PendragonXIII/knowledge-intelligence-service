# ######################################
# Knowledge Maintenance Service
# ######################################

class KnowledgeMaintenanceService:

    # ######################################
    # Generate Recommendations
    # ######################################

    def generate_recommendations(
        self,
        comparison_result: dict
    ):

        recommendations = []

        for object_id in comparison_result[
            "existing"
        ]:

            recommendations.append(
                {
                    "action":
                        "ignore",

                    "object_id":
                        object_id
                }
            )

        for object_id in comparison_result[
            "missing"
        ]:

            recommendations.append(
                {
                    "action":
                        "create",

                    "object_id":
                        object_id
                }
            )

        return recommendations
    
    # ######################################
    # Generate Maintenance Plan
    # ######################################

    def generate_maintenance_plan(
        self,
        recommendations: list
    ):

        plans = []

        folder_mapping = {

            "EID":
                "Capabilities",

            "CNS":
                "Constraints",

            "OP":
                "Opportunities",

            "LRN":
                "Learnings"
        }

        for recommendation in recommendations:

            object_id = recommendation[
                "object_id"
            ]

            prefix = (
                object_id.split(
                    "."
                )[0]
            )

            plans.append(
                {

                    "action":
                        recommendation[
                            "action"
                        ],

                    "object_id":
                        object_id,

                    "folder":
                        folder_mapping.get(
                            prefix
                        )
                }
            )

        return plans
    
    # ######################################
    # Generate File Template
    # ######################################

    def generate_file_template(
        self,
        object_id: str
    ):

        return f"""## Standard

    [[KTS.000 Knowledge Standard Standard]]

    ## Purpose

    TODO

    ## Current State

    Draft

    ## Related

    """

    # ######################################
    # Generate Maintenance Actions
    # ######################################

    def generate_maintenance_actions(
        self,
        comparison_result: dict
    ):

        actions = []

        for object_id in comparison_result[
            "existing"
        ]:

            actions.append(
                {
                    "action":
                        "update",

                    "object_id":
                        object_id
                }
            )

        for object_id in comparison_result[
            "missing"
        ]:

            actions.append(
                {
                    "action":
                        "create",

                    "object_id":
                        object_id
                }
            )

        return actions
    
    # ######################################
    # Generate Update Plan
    # ######################################

    def generate_update_plan(
        self,
        object_id: str,
        change_type: str
    ):

        action_mapping = {

            "relationship":
                "add_relationship",

            "append":
                "append_section",

            "replace":
                "replace_section",

            "rewrite":
                "rewrite_content"
        }

        return {

            "object_id":
                object_id,

            "action":
                action_mapping.get(
                    change_type
                )
        }
    
    # ######################################
    # Add Relationship
    # ######################################

    def add_relationship(
        self,
        relationships: list,
        relationship: str
    ):

        if relationship not in relationships:

            relationships.append(
                relationship
            )

        return relationships
    
    # ######################################
    # Append Bullet
    # ######################################

    def append_bullet(
        self,
        bullets: list,
        bullet: str
    ):

        formatted_bullet = (
            f"- {bullet}"
        )

        if formatted_bullet not in bullets:

            bullets.append(
                formatted_bullet
            )

        return bullets
    
    # ######################################
    # Append Section
    # ######################################

    def append_section(
        self,
        content: str,
        section_content: str
    ):

        if section_content not in content:

            if not content.endswith(
                "\n"
            ):

                content += "\n"

            content += (
                "\n"
                + section_content
            )

        return content
    
    # ######################################
    # Replace Section
    # ######################################

    def replace_section(
        self,
        content: str,
        old_section: str,
        new_section: str
    ):

        return content.replace(
            old_section,
            new_section
        )
    
    # ######################################
    # Rewrite Content
    # ######################################

    def rewrite_content(
        self,
        content: str
    ):

        return content
    
    # ######################################
    # Generate Repository Modification
    # ######################################

    def generate_repository_modification(
        self,
        action: dict
    ):

        object_id = action[
            "object_id"
        ]

        if object_id.startswith(
            "LRN."
        ):

            folder = (
                "Learnings"
            )

        elif object_id.startswith(
            "EID."
        ):

            folder = (
                "Capabilities"
            )

        else:

            folder = (
                "Unknown"
            )

        return {

            "operation":
                "create_file",

            "path":
                f"{folder}/"
                f"{object_id}.md"
        }
    
    # ######################################
    # Create File Modification
    # ######################################

    def create_file_modification(
        self,
        object_id: str
    ):

        template = (
            self.generate_file_template(
                object_id
            )
        )

        if object_id.startswith(
            "LRN."
        ):

            folder = (
                "Learnings"
            )

        elif object_id.startswith(
            "EID."
        ):

            folder = (
                "Capabilities"
            )

        else:

            folder = (
                "Unknown"
            )

        return {

            "path":
                f"{folder}/"
                f"{object_id}.md",

            "content":
                template
        }
    
    # ######################################
    # Generate Write Request
    # ######################################

    def generate_write_request(
        self,
        repository: str,
        modification: dict
    ):

        return {

            "repository":
                repository,

            "path":
                modification[
                    "path"
                ],

            "content":
                modification[
                    "content"
                ]
        }
    
    # ######################################
    # Generate File Update Request
    # ######################################

    def generate_file_update_request(
        self,
        path: str,
        content: str
    ):

        return {

            "operation":
                "update_file",

            "path":
                path,

            "content":
                content
        }