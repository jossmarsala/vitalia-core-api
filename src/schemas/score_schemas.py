from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial
from typing import List
from .paginated_schemas import PaginationMeta


class NewScoreRequest(BaseModel):
    planes_alimenticios: list[dict] = Field(..., min_length=4, max_length=6)
    rutinas: list[dict] = Field(..., min_length=4, max_length=6)
    articulos: list[dict] = Field(..., min_length=4, max_length=6)


class UpdateScoreRequest(Partial[NewScoreRequest]):
    pass


class ScoreResponse(BaseModel):
    uid: int
    planes_alimenticios: list[dict]
    rutinas: list[dict]
    articulos: list[dict]
    createdAt: str


class ScorePaginatedResponse(BaseModel):
    results: List[ScoreResponse]
    meta: PaginationMeta
