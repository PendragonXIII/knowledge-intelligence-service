import os


# ######################################
# GitHub Configuration Service
# ######################################

class GitHubConfigurationService:

    # ######################################
    # Get GitHub Token
    # ######################################

    def get_github_token(
        self
    ):

        return os.getenv(
            "GITHUB_TOKEN"
        )
    
    # ######################################
    # Has GitHub Token
    # ######################################

    def has_github_token(
        self
    ):

        return (
            self.get_github_token()
            is not None
        )