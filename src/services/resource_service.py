import logging
from typing import Optional

from src.exceptions import app_exceptions as ae
from src.repositories.resource_repository import ResourceRepository
from src.schemas.resource_schemas import ResourceResponse, ResourcePaginatedResponse

logger = logging.getLogger(__name__)


class ResourceService:
    def __init__(self, resource_repo: ResourceRepository = ResourceRepository()):
        self.resource_repo = resource_repo

    async def get_paginated(self, limit: int, start_after: Optional[str] = None) -> ResourcePaginatedResponse:
        logger.debug(f'Obteniendo recursos paginados. Límite: {limit}, start_after: {start_after}')

        raw_resources = await self.resource_repo.list(limit=limit, start_after=start_after)
        resources = [ResourceResponse.model_validate(r) for r in raw_resources]

        next_cursor = None
        if len(resources) == limit:
            last_resource = raw_resources[-1]
            next_cursor = last_resource.get("id")  # Asegurate de tener el ID en el dict

        logger.debug(f'{len(resources)} recursos obtenidos.')
        return ResourcePaginatedResponse(
            results=resources,
            meta={
                "items_per_page": limit,
                "next_cursor": next_cursor,
                "has_next_page": next_cursor is not None
            }
        )