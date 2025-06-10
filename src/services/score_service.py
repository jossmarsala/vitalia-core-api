import logging

from typing import Any, Dict

from .user_service import UserService
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
    def __init__(self, score_repo: ScoreRepository = ScoreRepository(), user_service: UserService = UserService()):
        self.score_repo = score_repo
        self.user_service = user_service

    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        logger.debug(f'Obteniendo puntajes paginados. Página: {page}, Límite: {limit}')
        raw_scores = self.score_repo.get_paginated(page, limit)

        results = []
        for score_data in raw_scores:
            uid = score_data["id"]
            user_data = await self.user_service.get_by_id(uid)
            full_name = f"{user_data.get('firstName', '')} {user_data.get('lastName', '')}".strip()
            score_data["user_full_name"] = full_name
            results.append(ScoreResponse.model_validate(score_data))

        total_count = self.score_repo.count()
        total_pages = max((total_count // limit) + (1 if total_count % limit else 0), 1)

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')

        return ScorePaginatedResponse(
            results=results,
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
        raw = await self.score_repo.create(data.model_dump(mode='json'))
        logger.debug(f'Puntaje creado: {raw}')
        return ScoreResponse.model_validate(raw)

    async def get_by_id(self, score_id: int) -> ScoreResponse:
        logger.debug(f'Obteniendo puntaje por ID: {score_id}')
        raw = await self.score_repo.get_by_id(score_id)
        if raw is None:
            raise ae.NotFoundError(f'El puntaje #{score_id} no existe')
        return ScoreResponse.model_validate(raw)

    async def update(self, score_id: int, data: UpdateScoreRequest) -> ScoreResponse:
        logger.debug(f'Actualizando puntaje #{score_id} con datos: {data}')
        payload: Dict[str, Any] = data.model_dump(mode='json', exclude_unset=True)

        for key in ["planes_alimenticios", "rutinas", "articulos"]:
            if key in payload and isinstance(payload[key], list):
                payload[key] = [
                    item if isinstance(item, dict) else item 
                    for item in payload[key]
                ]

        raw = await self.score_repo.update(score_id, payload)
        if raw is None:
            raise ae.NotFoundError(f'El puntaje #{score_id} no existe')
        return ScoreResponse.model_validate(raw)

    async def delete(self, score_id: int) -> None:
        logger.debug(f'Eliminando puntaje #{score_id}')
        deleted = await self.score_repo.delete(score_id)
        if not deleted:
            raise ae.NotFoundError(f'El puntaje #{score_id} no existe')
        return None