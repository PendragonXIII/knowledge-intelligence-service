from pydantic import BaseModel

class Relationship(BaseModel):
    source_id: str
    target_id: str
    relationship_type: str