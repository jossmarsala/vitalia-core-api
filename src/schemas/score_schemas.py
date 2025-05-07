from pydantic import BaseModel, Field
from typing import Optional

class NewScoreRequest(BaseModel):
        planes_alimenticios: list[dict] = Field(..., min_length=4, max_length=6)
        rutinas: list[dict] = Field(..., min_length=4, max_length=6)
        articulos: list[dict] = Field(..., min_length=4, max_length=6)

class UpdateScoreRequest(BaseModel):
        planes_alimenticios: Optional[list[dict]] = Field(None, min_length=4, max_length=6)
        rutinas: Optional[list[dict]] = Field(None, min_length=4, max_length=6)
        articulos: Optional[list[dict]] = Field(None, min_length=4, max_length=6)

class ScoreResponse(BaseModel):
        id: int
        planes_alimenticios: list[dict]
        rutinas: list[dict]
        articulos: list[dict]