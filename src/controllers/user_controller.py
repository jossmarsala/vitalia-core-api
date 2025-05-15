import logging

from src.exceptions.server_exceptions import InternalServerError, BaseHTTPException
from src.exceptions.client_exception import NotFound
import src.exceptions.app_exceptions as ae
from src.schemas.user_schemas import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserPaginatedResponse
)

logger = logging.getLogger(__name__)

class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    async def get_paginated(self, page: int, limit: int) -> UserPaginatedResponse:
        try:
            return await self.user_service.get_paginated(page, limit)
        except ae.NotFoundError as ex:
            logger.error(f'Página {page} no encontrada. Items por página: {limit}')
            raise NotFound(ex.message, 'USER_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al listar usuarios: {ex}')
            raise InternalServerError(
                message='Error al listar usuario',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def create(self, data: NewUserRequest) -> UserResponse:
        try:
            return await self.user_service.create(data)
        except ae.NotFoundError as ex:
            logger.error(f'No se pudo crear el usuario: {data.name}')
            raise NotFound(ex.message, 'USER_CREATE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al crear usuario "{data.name}": {ex}')
            raise InternalServerError(
                message=f'Error al crear usuario "{data.name}"',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def get_by_id(self, user_id: int) -> UserResponse:
        try:
            return await self.user_service.get_by_id(user_id)
        except ae.NotFoundError as ex:
            logger.error(f'Usuario #{user_id} no encontrado')
            raise NotFound(ex.message, 'USER_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al obtener usuario #{user_id}: {ex}')
            raise InternalServerError(
                message=f'Error al obtener usuario #{user_id}',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def update(self, user_id: int, data: UpdateUserRequest) -> UserResponse:
        try:
            return await self.user_service.update(user_id, data)
        except ae.NotFoundError as ex:
            logger.error(f'Usuario #{user_id} no encontrado')
            raise NotFound(ex.message, 'USER_UPDATE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al actualizar usuario #{user_id}: {ex}')
            raise InternalServerError(
                message=f'Error al actualizar usuario #{user_id}',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def delete(self, user_id: int) -> None:
        try:
            return await self.user_service.delete(user_id)
        except ae.NotFoundError as ex:
            logger.error(f'Usuario #{user_id} no encontrado')
            raise NotFound(ex.message, 'USER_DELETE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error desconocido al eliminar usuario #{user_id}: {ex}')
            raise InternalServerError(
                message=f'Error al eliminar usuario #{user_id}',
                exception_code='USER_UNHANDLED_ERROR'
            )
