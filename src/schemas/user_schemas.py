from typing import List

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from src.schemas.paginated_schemas import PaginationMeta


class NewUserRequest(BaseModel):
    mail: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=8)


class UpdateUserRequest(Partial[NewUserRequest]):
    pass


class UserResponse(BaseModel):
    uid: str
    mail: str


class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
