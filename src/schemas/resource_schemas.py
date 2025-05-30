from pydantic import BaseModel, Field
from typing import Dict, Any, List

from src.schemas.paginated_schemas import PaginationMeta

class ResourceResponse(BaseModel):
    title: str = Field(...)
    data: Dict[str, Any] = Field(...)

class ResourcePaginatedResponse(BaseModel):
    results: List[ResourceResponse]
    meta: PaginationMeta