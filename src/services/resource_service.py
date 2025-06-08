import logging
from typing import List

from src.exceptions import app_exceptions as ae
from src.repositories.resource_repository import ResourceRepository
from src.schemas.resource_schemas import ResourceResponse, ResourcePaginatedResponse

logger = logging.getLogger(__name__)


class ResourceService:
    def __init__(self, resource_repo: ResourceRepository = ResourceRepository()):
        self.resource_repo = resource_repo

    async def get_paginated(self, page: int, limit: int) -> ResourcePaginatedResponse:
        logger.debug(f'Obteniendo recursos paginados. Página: {page}, Límite: {limit}')

        raw_resources = self.resource_repo.get_paginated(page=page, limit=limit)
        resources: List[ResourceResponse] = []
        for idx, r in enumerate(raw_resources):
            try:
                validated = ResourceResponse.model_validate(r)
                resources.append(validated)
            except Exception as e:
                logger.error(f"No se pudo validar el recurso #{idx}: {r}")
                logger.exception(e)

        total_count = self.resource_repo.count()

        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages
        if page > total_pages:
            raise ae.NotFoundError(f'La página {page} no existe')

        has_previous = page > 1
        has_next = page < total_pages

        logger.debug(f'Recursos validados: {len(resources)} de {total_count} totales.')
        return ResourcePaginatedResponse(
            results=resources,
            meta={
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "items_per_page": limit,
                "has_previous_page": has_previous,
                "has_next_page": has_next
            }
        )
