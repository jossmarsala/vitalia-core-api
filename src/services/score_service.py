from typing import List
import asyncio

from src.exceptions import app_exceptions as ae
from src.schemas.paginated_schemas import PaginationMeta
from src.schemas.score_schemas import (
    NewScoreRequest,
    UpdateScoreRequest,
    ScoreResponse,
    ScorePaginatedResponse
)


class ScoreService():
    def __init__(self, score_repo):
        self.score_repo = score_repo

    # CRUD
    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        score, total_count = await asyncio.gather(
            self.__get_score_list(page, limit),
            self.__count()
        )
        total_pages = (total_count // limit) + \
            (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError()

        return ScorePaginatedResponse(
            results=score,
            meta= PaginationMeta(
                current_page=page,
                total_pages=total_pages,
                total_items=total_count,
                items_per_page=limit,
                has_previous_page=page > 1,
                has_next_page=page < total_pages
            )
        )

    async def create(self, data: NewScoreRequest) -> ScoreResponse:
        return ScoreResponse(
            id=1,
            planes_alimenticios=data.planes_alimenticios,
            rutinas=data.rutinas,
            articulos=data.articulos
        )

    async def get_by_id(self, score_id: int) -> ScoreResponse:
        raise ae.NotFoundError(f"El puntaje #{score_id} no existe")

    async def update(self, score_id: int, data: UpdateScoreRequest) -> ScoreResponse:
        raise ae.NotFoundError(f"El puntaje #{score_id} no existe")

    async def delete(self, score_id: int) -> None:
        raise ae.NotFoundError(f"El puntaje #{score_id} no existe")

    async def __count(self) -> int:
        # TODO: Llamar al repo y devolver el total
        return 0

    async def __get_score_list(self, page: int, limit: int) -> List[ScoreResponse]:
        # TODO: Llamar al repo y obtener listado
        return []
