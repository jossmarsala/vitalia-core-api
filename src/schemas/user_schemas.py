from typing import List

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from src.schemas.paginated_schemas import PaginationMeta


class NewUserRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Josefina")
    mail: str = Field(..., min_length=5, max_length=100, example="mail@ejemplo.com")
    password: str = Field(..., min_length=8, example="contraseña-123")


class UpdateUserRequest(Partial[NewUserRequest]):
    pass


class UserResponse(BaseModel):
    uid: str
    mail: str


class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
