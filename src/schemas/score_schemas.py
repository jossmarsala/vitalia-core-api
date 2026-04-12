from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial
from typing import List
from .paginated_schemas import PaginationMeta


class NewScoreRequest(BaseModel):
    id: str = Field(...)
    planes_alimenticios: list[str] = Field(..., min_length=4, max_length=6)
    rutinas: list[str] = Field(..., min_length=4, max_length=6)
    articulos: list[str] = Field(..., min_length=4, max_length=6)


class UpdateScoreRequest(Partial[NewScoreRequest]):
    pass


class ScoreResponse(BaseModel):
    id: str
    planes_alimenticios: list[str]
    rutinas: list[str]
    articulos: list[str]
    createdAt: str
    updatedAt: str


class ScorePaginatedResponse(BaseModel):
    results: List[ScoreResponse]
    meta: PaginationMeta
