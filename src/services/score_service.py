import asyncio
import logging
from typing import List

from src.exceptions import app_exceptions as ae
from src.repositories.score_repository import ScoreRepository
from src.schemas.score_schemas import (
    NewScoreRequest,
    UpdateScoreRequest,
    ScoreResponse,
    ScorePaginatedResponse
)

logger = logging.getLogger(__name__)


class ScoreService():
    def __init__(self, score_repo: ScoreRepository = ScoreRepository()):
        self.score_repo = score_repo

    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        logger.debug(f'Obteniendo puntajes paginados. Página: {page}, Límite: {limit}')
        scores, total_count = await asyncio.gather(
            self.__get_score_list(page, limit),
            self.__count()
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')

        logger.debug(f'Puntajes obtenidos: {len(scores)}')
        return ScorePaginatedResponse(
            results=scores,
            meta={
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "items_per_page": limit,
                "has_previous_page": page > 1,
                "has_next_page": page < total_pages
            }
        )

    async def create(self, data: NewScoreRequest) -> ScoreResponse:
        logger.debug(f'Creando puntaje: {data}')
        new_score = await self.score_repo.create(data.model_dump(mode='json'))
        logger.debug(f'Puntaje creado: {new_score}')
        return ScoreResponse.model_validate(new_score)

    async def get_by_id(self, score_id: int) -> ScoreResponse:
        logger.debug(f'Obteniendo puntaje por ID: {score_id}')
        score = await self.score_repo.get_one_by_criteria({'id': score_id})
        if score is None:
            raise ae.NotFoundError(f"El puntaje #{score_id} no existe")
        return ScoreResponse.model_validate(score)

    async def update(self, score_id: int, data: UpdateScoreRequest) -> ScoreResponse:
        logger.debug(f'Actualizando puntaje #{score_id} con datos: {data}')
        updated_score = await self.score_repo.update_one(
            {'id': score_id},
            data.model_dump(mode='json', exclude_unset=True)
        )
        if updated_score is None:
            raise ae.NotFoundError(f"El puntaje #{score_id} no existe")
        return ScoreResponse.model_validate(updated_score)

    async def delete(self, score_id: int) -> None:
        logger.debug(f'Eliminando puntaje #{score_id}')
        deleted = await self.score_repo.delete_one({'id': score_id})
        if not deleted:
            raise ae.NotFoundError(f"El puntaje #{score_id} no existe")
        return None

    async def __count(self) -> int:
        return await self.score_repo.count()

    async def __get_score_list(self, page: int, limit: int) -> List[ScoreResponse]:
        return await self.score_repo.get_many(page, limit)
