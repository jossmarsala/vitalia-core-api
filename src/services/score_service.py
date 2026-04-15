import logging

from typing import Any, Dict, List
from datetime import datetime

from .user_service import UserService
from src.exceptions import app_exceptions as ae
from src.repositories.score_repository import ScoreRepository
from src.repositories.user_repository import UserRepository
from src.repositories.resource_repository import ResourceRepository
from src.schemas.score_schemas import (
    NewScoreRequest,
    UpdateScoreRequest,
    ScoreResponse,
    ScorePaginatedResponse
)

logger = logging.getLogger(__name__)


class ScoreService():
    def __init__(self, score_repo: ScoreRepository = ScoreRepository(), resource_repo: ResourceRepository = ResourceRepository(), user_repo: UserRepository = UserRepository(), user_service: UserService = UserService):
        self.score_repo = score_repo
        self.resource_repo = resource_repo
        self.user_repo = user_repo
        self.user_service = user_service

    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        logger.debug(f'Obteniendo puntajes paginados. Página: {page}, Límite: {limit}')

        raw_scores = self.score_repo.get_paginated(page=page, limit=limit)
        scores: List[ScoreResponse] = []
        for idx, r in enumerate(raw_scores):
            try:
                validated = ScoreResponse.model_validate(r)
                scores.append(validated)
            except Exception as e:
                logger.error(f"No se pudo validar el puntaje #{idx}: {r}")
                logger.exception(e)

        total_count = self.score_repo.count()

        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages
        if page > total_pages:
            raise ae.NotFoundError(f'La página {page} no existe')

        has_previous = page > 1
        has_next = page < total_pages

        logger.debug(f'Puntajes validados: {len(scores)} de {total_count} totales.')
        return ScorePaginatedResponse(
            results=scores,
            meta={
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "items_per_page": limit,
                "has_previous_page": has_previous,
                "has_next_page": has_next
            }
        )


    async def create(self, data: NewScoreRequest) -> ScoreResponse:
        logger.debug(f'Creando puntaje manualmente: {data}')
        raw = await self.score_repo.create(data.model_dump(mode='json'))
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
        
    async def match_and_create(self, uid: str, user_data: dict) -> ScoreResponse:
        logger.info(f'[Score] Iniciando recomendación para uid={uid}')
        
        from src.recommendation.engine import recommend
        result = recommend(user_data)

        logger.info(f'[Score] Resultado del engine: diets={result.diets}, routines={result.routines}, articles={result.articles}')

        score_obj = {
            "id": uid,
            "planes_alimenticios": result.diets,
            "rutinas": result.routines,
            "articulos": result.articles,
        }

        logger.info(f'[Score] Guardando en Firestore con doc_id={uid}')
        raw = await self.score_repo.create_with_id(uid, score_obj)
        logger.info(f'[Score] Guardado correctamente: {raw}')

        return ScoreResponse.model_validate(raw)

    async def generate(self, uid: str, user_prefs: dict) -> ScoreResponse:
        """
        Genera y persiste las recomendaciones para un usuario ya registrado.
        Llamado directamente desde el frontend tras el registro con Firebase Auth.

        Args:
            uid: Firebase Auth UID del usuario (usado como doc ID en 'scores').
            user_prefs: Respuestas del cuestionario (disability, physicalActivity, etc.)
        """
        logger.info(f'[Score] generate() llamado para uid={uid}')

        # Verificar si ya existe un score para este uid (idempotencia)
        existing = await self.score_repo.get_by_id(uid)
        if existing:
            logger.info(f'[Score] Ya existe un score para uid={uid}, sobreescribiendo.')

        from src.recommendation.engine import recommend
        result = recommend(user_prefs)

        logger.info(
            f'[Score] Engine result — diets={result.diets}, '
            f'routines={result.routines}, articles={result.articles}'
        )

        score_obj = {
            "id": uid,
            "planes_alimenticios": result.diets,
            "rutinas": result.routines,
            "articulos": result.articles,
        }

        raw = await self.score_repo.create_with_id(uid, score_obj)
        logger.info(f'[Score] Score guardado en Firestore para uid={uid}')
        return ScoreResponse.model_validate(raw)