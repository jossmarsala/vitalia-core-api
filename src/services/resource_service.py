import asyncio
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
        logger.debug(
            f'Obteniendo recursos paginados. Página: {page}, Límite: {limit}')
        resources, total_count = await asyncio.gather(
            self.__get_resource_list(page, limit),
            self.__count_resources()
        )

        total_pages = (total_count // limit) + \
            (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')

        logger.debug(f'Recursos obtenidos: {len(resources)}')
        return ResourcePaginatedResponse(
            results=resources,
            meta={
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "items_per_page": limit,
                "has_previous_page": page > 1,
                "has_next_page": page < total_pages
            }
        )

    async def __get_resource_list(self, page: int, limit: int) -> List[ResourceResponse]:
        raw = await self.resource_repo.list(page=page, limit=limit)
        return [ResourceResponse.model_validate(r) for r in raw]

    async def __count_resources(self) -> int:
        return await self.resource_repo.count()
