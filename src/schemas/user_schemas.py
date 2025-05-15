from typing import List

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from src.schemas.paginated_schemas import PaginationMeta


class NewUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)


class UpdateUserRequest(Partial[NewUserRequest]):
    pass


class UserResponse(BaseModel):
    id: int
    username: str


class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
