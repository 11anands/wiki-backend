from typing import List
from datetime import date
from pydantic import BaseModel
from uuid import UUID

# Schema for Search Value
class SearchValueSchema(BaseModel):
    name: str


# Schema for Drugs
class DrugsSchema(BaseModel):
    id: UUID
    name: str
    diseases: List[str]
    description: str
    released: date

# Schema for History
class HistorySchema(BaseModel):
    id: int
    name: str
    is_created: date




