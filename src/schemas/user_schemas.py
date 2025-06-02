from typing import List, Any

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from src.schemas.paginated_schemas import PaginationMeta


class NewUserRequest(BaseModel):
    age: str = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    gender: str = Field(...)
    email: str = Field(...)
    country: str = Field(...)
    dailyRoutine: str = Field(...) 
    diet: str = Field(...) 
    disability: str = Field(...) 
    lifestyle: str = Field(...) 
    obstacles: List[str] = Field(...) 
    physicalActivity: str = Field(...) 
    restrictions: List[str] = Field(...) 
    sleepQuality: str = Field(...) 
    stressLevel: str = Field(...) 
    wellbeingGoals: List[str] = Field(...)
    

class UpdateUserRequest(Partial[NewUserRequest]):
    pass


class UserResponse(BaseModel): 
    age: str 
    firstName: str 
    lastName: str 
    gender: str 
    email: str 
    country: str 
    createdAt: Any  
    updatedAt: Any
    dailyRoutine: str  
    diet: str  
    disability: str  
    lifestyle: str  
    obstacles: List[str]  
    physicalActivity: str  
    restrictions: List[str]  
    sleepQuality: str  
    stressLevel: str  
    wellbeingGoals: List[str] 


class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
