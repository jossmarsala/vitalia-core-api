from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial
from typing import List, Optional
from .paginated_schemas import PaginationMeta


class GenerateScoreRequest(BaseModel):
    """
    Payload enviado por el frontend después del registro para generar
    las recomendaciones. El uid corresponde al Firebase Auth UID.
    """
    uid: str = Field(..., description="Firebase Auth UID del usuario recién registrado")
    disability: Optional[str] = None
    physicalActivity: Optional[str] = None
    diet: Optional[str] = None
    restrictions: List[str] = Field(default_factory=list)
    wellbeingGoals: List[str] = Field(default_factory=list)
    obstacles: List[str] = Field(default_factory=list)
    sleepQuality: Optional[str] = None
    stressLevel: Optional[str] = None
    dailyRoutine: Optional[str] = None
    lifestyle: Optional[str] = None


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
