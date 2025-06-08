from pydantic import BaseModel
from typing import List, Optional

from src.schemas.paginated_schemas import PaginationMeta

class ResourceResponse(BaseModel):
    id: Optional[str] = None
    dailyRoutine: Optional[str] = None 
    diet: Optional[str] = None 
    disability: Optional[str] = None 
    lifestyle: Optional[str] = None 
    obstacles: Optional[str] = None
    physicalActivity: Optional[str] = None 
    restrictions: Optional[str] = None
    sleepQuality: Optional[str] = None 
    stressLevel: Optional[str] = None 
    wellbeingGoals: Optional[str] = None

class ResourcePaginatedResponse(BaseModel):
    results: List[ResourceResponse]
    meta: PaginationMeta