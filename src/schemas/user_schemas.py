from pydantic import BaseModel, Field
from typing import Optional, List
from src.schemas.paginated_schemas import PaginationMeta


class NewUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)
    name: str = Field(..., min_length=1)
    email: str = Field(..., regex=r'^\S+@\S+\.\S+$')


class UpdateUserRequest(BaseModel):
    password: Optional[str] = Field(None, min_length=8)
    name: Optional[str] = Field(None, min_length=1)
    email: Optional[str] = Field(None, regex=r'^\S+@\S+\.\S+$')


class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    email: str


class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
