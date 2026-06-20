import os

import requests

import base64

from app.services.github_configuration_service import (
    GitHubConfigurationService
)


# ######################################
# GitHub Repository Service
# ######################################

class GitHubRepositoryService:

    def __init__(self):

        self.owner = "PendragonXIII"

        self.repository = (
            "Knowledge-Intelligence-Platform"
        )

        configuration_service = (
            GitHubConfigurationService()
        )

        self.configuration_service = (
            configuration_service
        )

        self.token = (
            configuration_service.get_github_token()
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
    # Has GitHub Token
    # ######################################

    def has_github_token(
        self
    ):

        return (
            self.configuration_service
            .has_github_token()
        )

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

    # ######################################
    # Find Object
    # ######################################

    def find_object(
        self,
        object_id: str
    ):

        folders = [
            "Capabilities",
            "Contraints",
            "Standards",
            "Playbooks",
            "Roadmaps",
            "Opportunities",
            "Learnings",
            "Architectual Decisions"
        ]

        for folder in folders:

            try:

                items = self.get_folder_content(
                    folder
                )

                for item in items:

                    if item[
                        "name"
                    ].startswith(
                        object_id
                    ):
                        return item[
                            "path"
                        ]

            except Exception as e:

                print(
                    f"Folder Error: {folder}"
                )

                print(
                    str(e)
                )

                raise

        raise FileNotFoundError(
            f"Knowledge Object not found: {object_id}"
        )
    
    # ######################################
    # Get File Content
    # ######################################

    def get_file_content(
        self,
        path: str
    ):

        response = requests.get(
            f"{self.base_url}/"
            f"{self.owner}/"
            f"{self.repository}/contents/"
            f"{path}",
            headers=self._headers()
        )

        response.raise_for_status()

        data = response.json()

        download_url = data[
            "download_url"
        ]

        content_response = requests.get(
            download_url
        )

        content_response.raise_for_status()

        return content_response.text
    
    # ######################################
    # Get File By Path
    # ######################################

    def get_file_by_path(
        self,
        path: str,
        repository: str | None = None
    ):

        repository_name = (
            repository
            if repository
            else self.repository
        )

        response = requests.get(
            f"{self.base_url}/"
            f"{self.owner}/"
            f"{repository_name}/contents/"
            f"{path}",
            headers=self._headers()
        )

        response.raise_for_status()

        data = response.json()

        download_url = data[
            "download_url"
        ]

        content_response = requests.get(
            download_url
        )

        content_response.raise_for_status()

        return content_response.text
    
    # ######################################
    # Get File Metadata
    # ######################################

    def get_file_metadata(
        self,
        path: str,
        repository: str | None = None
    ):

        repository_name = (
            repository
            if repository
            else self.repository
        )

        response = requests.get(
            f"{self.base_url}/"
            f"{self.owner}/"
            f"{repository_name}/contents/"
            f"{path}",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()
        
    # ######################################
    # Create File
    # ######################################

    def create_file(
        self,
        path: str,
        content: str,
        message: str
    ):

        encoded_content = (
            base64.b64encode(
                content.encode(
                    "utf-8"
                )
            )
            .decode(
                "utf-8"
            )
        )

        response = requests.put(
            f"{self.base_url}/"
            f"{self.owner}/"
            f"{self.repository}/contents/"
            f"{path}",

            headers=self._headers(),

            json={

                "message":
                    message,

                "content":
                    encoded_content
            }
        )

        response.raise_for_status()

        return response.json()
    
    # ######################################
    # Update File
    # ######################################

    def update_file(
        self,
        path: str,
        content: str,
        sha: str | None,
        message: str
    ):

        import base64

        if not sha:

            metadata = (
                self.get_file_metadata(
                    path
                )
            )

            sha = metadata[
                "sha"
            ]

        encoded_content = (
            base64.b64encode(
                content.encode(
                    "utf-8"
                )
            )
            .decode(
                "utf-8"
            )
        )

        response = requests.put(

            f"{self.base_url}/"
            f"{self.owner}/"
            f"{self.repository}/contents/"
            f"{path}",

            headers=self._headers(),

            json={

                "message":
                    message,

                "content":
                    encoded_content,

                "sha":
                    sha
            }
        )

        response.raise_for_status()

        return response.json()