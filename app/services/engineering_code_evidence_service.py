class EngineeringCodeEvidenceService:

    def __init__(self):

        self.repository_client = None

    # ######################################
    # Repository File
    # ######################################

    def get_repository_file(
        self,
        path: str
    ):

        return (
            self.repository_client
            .get_repository_file(
                path
            )
        )

    # ######################################
    # Module Context
    # ######################################

    def get_module_context(
        self,
        module_name: str
    ):

        return (
            self.repository_client
            .get_module_context(
                module_name
            )
        )

    # ######################################
    # Repository Search
    # ######################################

    def search_repository(
        self,
        query: str
    ):

        return (
            self.repository_client
            .search_repository(
                query
            )
        )