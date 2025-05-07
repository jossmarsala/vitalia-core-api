from pydantic import BaseModel, Field
from typing import Optional

class NewScoreRequest(BaseModel):
        planes_alimenticios: list = Field(..., min_length=4, max_length=6)
        rutinas: list = Field(..., min_length=4, max_length=6)
        articulos: list = Field(..., min_length=4, max_length=6)

class UpdateScoreRequest(BaseModel):
        planes_alimenticios: Optional[list] = Field(None, min_length=4, max_length=6)
        rutinas: Optional[list] = Field(None, min_length=4, max_length=6)
        articulos: Optional[list] = Field(None, min_length=4, max_length=6)