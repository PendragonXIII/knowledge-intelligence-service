import os

import requests


# ######################################
# GitHub Repository Service
# ######################################

class GitHubRepositoryService:

    def __init__(self):

        self.owner = "PendragonXIII"

        self.repository = (
            "Knowledge-Intelligence-Platform"
        )

        self.token = os.getenv(
            "GITHUB_TOKEN"
        )

        self.base_url = (
            "https://api.github.com/repos"
        )

    # ######################################
    # Headers
    # ######################################

    def _headers(self):

        return {
            "Authorization":
                f"Bearer {self.token}",

            "Accept":
                "application/vnd.github+json"
        }

    # ######################################
    # List Root Content
    # ######################################

    def get_root_content(self):

        response = requests.get(
            f"{self.base_url}/"
            f"{self.owner}/"
            f"{self.repository}/contents",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()
    
    # ######################################
    # Get Folder Content
    # ######################################

    def get_folder_content(
        self,
        folder_name: str
    ):

        response = requests.get(
            f"{self.base_url}/"
            f"{self.owner}/"
            f"{self.repository}/contents/"
            f"{folder_name}",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()
    
    # ######################################
    # Find Object
    # ######################################

    def find_object(
        self,
        object_id: str
    ):

        capabilities = self.get_folder_content(
            "Capabilities"
        )

        for item in capabilities:

            if item["name"].startswith(
                object_id
            ):
                return item["path"]

        raise FileNotFoundError(
            f"Knowledge Object not found: {object_id}"
        )