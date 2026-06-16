from pydantic import BaseModel
from typing import List


class KnowledgeObject(BaseModel):
    id: str
    title: str
    object_type: str
    content: str
    relationships: List[str] = []