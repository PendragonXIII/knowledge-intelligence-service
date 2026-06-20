from pydantic import BaseModel


class RepositoryWriteRequest(
    BaseModel
):

    path: str

    content: str