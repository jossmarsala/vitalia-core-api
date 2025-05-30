import logging

from src.exceptions.server_exceptions import InternalServerError, BaseHTTPException
from src.exceptions.client_exception import NotFound
from src.services.resource_service import ResourceService
from src.schemas.resource_schemas import (
    ResourceResponse, 
    ResourcePaginatedResponse
)

import src.exceptions.app_exceptions as ae
from src.exceptions.client_exception import NotFound


logger = logging.getLogger(__name__)

class ResourceController():
    def __init__(self, resource_service: ResourceService):
        self.resource_service = resource_service

    async def get_paginated(self, page: int, limit: int) -> ResourcePaginatedResponse:
        try:
            return await self.resource_service.get_paginated(page, limit)
        except ae.NotFoundError as ex:
            logger.error(f'Página {page} no encontrada. Items por página: {limit}')
            raise NotFound(ex.message, 'RESOURCE_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al listar recursos: {ex}')
            raise InternalServerError(
                message=f'Error al listar recursos',
                exception_code="RESOURCE_UNHANDLED_ERROR"
            )