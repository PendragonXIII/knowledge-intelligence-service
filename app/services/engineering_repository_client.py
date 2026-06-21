import requests


# ######################################
# Engineering Repository Client
# ######################################

class EngineeringRepositoryClient:

    def __init__(self):

        self.base_url = (
            "ENGINEERING_API_URL"
        )

    # ######################################
    # Search Repository
    # ######################################

    def search_repository(
        self,
        query: str
    ):

        response = requests.get(

            f"{self.base_url}/engineering/repository-search",

            params={

                "query":
                    query
            }
        )

        return (
            response.json()
        )
    
    # ######################################
    # Get Document Content
    # ######################################

    def get_document_content(
        self,
        filename: str
    ):

        response = requests.get(

            f"{self.base_url}/engineering/document-content",

            params={

                "filename":
                    filename
            }
        )

        return (
            response.json()
        )
    
    # ######################################    
    # Get Module Context
    # ######################################

    def get_module_context(
        self,
        module_name: str
    ):

        response = requests.get(

            f"{self.base_url}/engineering/module-context",

            params={

                "module_name":
                    module_name
            }
        )

        return (
            response.json()
        )