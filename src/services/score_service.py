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
        logger.debug(f'Matcheando preferencias para usuario {uid}')
        resources = self.resource_repo.get_paginated(page=1, limit=1000)

        user_prefs = {
            "sleepQuality": str(user_data.get("sleepQuality", "")).strip().lower(),
            "wellbeingGoals": [str(x).strip().lower() for x in user_data.get("wellbeingGoals", [])],
            "stressLevel": str(user_data.get("stressLevel", "")).strip().lower(),
            "restrictions": [str(x).strip().lower() for x in user_data.get("restrictions", [])],
            "obstacles": [str(x).strip().lower() for x in user_data.get("obstacles", [])],
            "dailyRoutine": str(user_data.get("dailyRoutine", "")).strip().lower(),
            "diet": str(user_data.get("diet", "")).strip().lower(),
            "disability": str(user_data.get("disability", "")).strip().lower(),
            "lifestyle": str(user_data.get("lifestyle", "")).strip().lower(),
            "physicalActivity": str(user_data.get("physicalActivity", "")).strip().lower(),
        }

        resource_scores = {}

        for resource in resources:
            doc_id = resource.get("id")
            score = 0
            for key, user_value in user_prefs.items():
                resource_value = resource.get(key)
                if isinstance(resource_value, list):
                    resource_value = [str(x).strip().lower() for x in resource_value]
                elif resource_value is not None:
                    resource_value = str(resource_value).strip().lower()
                else:
                    resource_value = None

                if isinstance(user_value, list):
                    if isinstance(resource_value, list):
                        matches = set(user_value) & set(resource_value)
                        score += len(matches)
                    elif isinstance(resource_value, str) and resource_value:
                        if resource_value in user_value:
                            score += 1

                elif user_value and resource_value and user_value == resource_value:
                    score += 1
            resource_scores[doc_id] = score

        planes_alimenticios = []
        rutinas = []
        articulos = []

        sorted_resources = sorted(resource_scores.items(), key=lambda x: x[1], reverse=True)

        for doc_id, points in sorted_resources:
            if doc_id.startswith("diet") and len(planes_alimenticios) < 4:
                planes_alimenticios.append({"resource_id": doc_id})
            elif doc_id.startswith("routine") and len(rutinas) < 4:
                rutinas.append({"resource_id": doc_id})
            elif doc_id.startswith("article") and len(articulos) < 4:
                articulos.append({"resource_id": doc_id})
            if len(planes_alimenticios) == 4 and len(rutinas) == 4 and len(articulos) == 4:
                break

        while len(planes_alimenticios) < 4:
            planes_alimenticios.append({"resource_id": {}})
        while len(rutinas) < 4:
            rutinas.append({"resource_id": {}})
        while len(articulos) < 4:
            articulos.append({"resource_id": {}})

        score_obj = {
            "id": uid,
            "planes_alimenticios": planes_alimenticios,
            "rutinas": rutinas,
            "articulos": articulos,
        }

        raw = await self.score_repo.create_with_id(uid, score_obj)
        return ScoreResponse.model_validate(raw)