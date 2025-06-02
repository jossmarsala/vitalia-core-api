from typing import List

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from src.schemas.paginated_schemas import PaginationMeta


class NewUserRequest(BaseModel):
    uid: str = Field(...)
    age: str = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    gender: str = Field(...)
    email: str = Field(...)
    country: str = Field(...)
    createdAt: str = Field(...) 
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
    uid: str = Field(...)
    age: str = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    gender: str = Field(...)
    email: str = Field(...)
    country: str = Field(...)
    createdAt: str = Field(...) 
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


class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
