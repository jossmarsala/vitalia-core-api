from pydantic import BaseModel, Field

class NewScoreRequest(BaseModel):
        planes_alimenticios: list = Field(..., min_length=4, max_length=6)
        rutinas: list = Field(..., min_length=4, max_length=6)
        articulos: list = Field(..., min_length=4, max_length=6)