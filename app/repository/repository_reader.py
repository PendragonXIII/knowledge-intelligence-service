from pathlib import Path

class RepositoryReader:

    def __init__(self, repository_path: str):
        self.repository_path = Path(repository_path)

    def read_file(self, filename: str) -> str:

        file_path = self.repository_path / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Knowledge Object not found: {filename}"
            )

        return file_path.read_text(
            encoding="utf-8"
        )
