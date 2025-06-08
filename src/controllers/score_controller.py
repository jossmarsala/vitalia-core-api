import logging

from src.exceptions.server_exceptions import InternalServerError, BaseHTTPException
from src.exceptions.client_exception import NotFound
from src.schemas.score_schemas import (
    NewScoreRequest, 
    UpdateScoreRequest, 
    ScoreResponse, 
    ScorePaginatedResponse
)

import src.exceptions.app_exceptions as ae
from src.exceptions.client_exception import NotFound

from src.services.score_service import ScoreService

logger = logging.getLogger(__name__)

class ScoreController():
    def __init__(self, score_service: ScoreService):
        self.score_service = score_service

    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        try:
            return await self.score_service.get_paginated(page, limit)
        except ae.NotFoundError as ex:
            logger.error(f'Página {page} no encontrada. Items por página: {limit}')
            raise NotFound(ex.message, 'SCORE_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al listar puntajes: {ex}')
            raise InternalServerError(
                message=f'Error al listar puntaje',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def create(self, data: NewScoreRequest) -> ScoreResponse:
        try:
            return await self.score_service.create(data)
        except ae.NotFoundError as ex:
            logger.error(f'Error al crear puntaje: {data.id}')
            raise NotFound(ex.message, 'SCORE_CREATE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al crear puntaje "{data.id}": {ex}')
            raise InternalServerError(
                message=f'Error al crear puntaje "{data.id}"',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def get_by_id(self, score_id: int) -> ScoreResponse:
        try:
            return await self.score_service.get_by_id(score_id)
        except ae.NotFoundError as ex:
            logger.error(f'Puntaje #{score_id} no encontrado dentro del método "get_by_id"')
            raise NotFound(ex.message, 'SCORE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al obtener puntaje #{score_id}: {ex}')
            raise InternalServerError(
                message=f'Error al obtener puntaje #{score_id}',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def update(self, score_id: int, data: UpdateScoreRequest) -> ScoreResponse:
        try:
            return await self.score_service.update(score_id, data)
        except ae.NotFoundError as ex:
            logger.error(f'Puntaje #{score_id} no encontrado dentro del método "update"')
            raise NotFound(ex.message, 'SCORE_UPDATE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al actualizar puntaje #{score_id}: {ex}')
            raise InternalServerError(
                message=f'Error al actualizar puntaje #{score_id}',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def delete(self, score_id: int) -> None:
        try:
            return await self.score_service.delete(score_id)
        except ae.NotFoundError as ex:
            logger.error(f'Puntaje #{score_id} no encontrado dentro del método "delete"')
            raise NotFound(ex.message, 'SCORE_DELETE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al eliminar puntaje #{score_id}: {ex}')
            raise InternalServerError(
                message=f'Error al eliminar puntaje #{score_id}',
                exception_code="SCORE_UNHANDLED_ERROR"
            )
