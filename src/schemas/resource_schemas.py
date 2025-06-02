from pydantic import BaseModel
from typing import List

from src.schemas.paginated_schemas import PaginationMeta

class ResourceResponse(BaseModel):
    dailyRoutine: str  
    diet: str  
    disability: str  
    lifestyle: str  
    obstacles: str 
    physicalActivity: str  
    restrictions: str 
    sleepQuality: str  
    stressLevel: str  
    wellbeingGoals: str

class ResourcePaginatedResponse(BaseModel):
    results: List[ResourceResponse]
    meta: PaginationMeta