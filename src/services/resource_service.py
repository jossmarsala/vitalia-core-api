import asyncio
import logging
from typing import List, Dict, Any

from src.repositories.resource_repository import ResourceRepository
from src.schemas.resource_schemas import ResourceResponse

logger = logging.getLogger(__name__)

class ResourceService:
    def __init__(
        self,
        resource_repo: ResourceRepository = ResourceRepository()
    ):
        self.resource_repo = resource_repo

    async def list_all(self) -> List[ResourceResponse]:
        logger.debug("Obteniendo recursos.")
        raw, total = await asyncio.gather(
            self.__get_resource_list(),
            self.__count_resources()
        )

        if total == 0:
            logger.warning("No se encontraron recursos.")
            return []

        logger.debug(f"Recursos obtenidos: {total}")
        return [ResourceResponse.model_validate(r) for r in raw]

    async def __get_resource_list(self) -> List[Dict[str, Any]]:
        return await self.resource_repo.get_all()

    async def __count_resources(self) -> int:
        return await self.resource_repo.count()
