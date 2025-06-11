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
            logger.error(
                f'Página {page} no encontrada. Items por página: {limit}')
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
            logger.error(f'No se pudo crear el usuario')
            raise NotFound(ex.message, 'USER_CREATE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(
                f'Error desconocido al crear usuario: {ex}')
            raise InternalServerError(
                message=f'Error al crear usuario',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def get_by_id(self, uid: str) -> UserResponse:
        try:
            return await self.user_service.get_by_id(uid)
        except ae.NotFoundError as ex:
            logger.error(f'Usuario {uid} no encontrado')
            raise NotFound(ex.message, 'USER_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(
                f'Error desconocido al obtener usuario {uid}: {ex}')
            raise InternalServerError(
                message=f'Error al obtener usuario {uid}',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def update_by_id(self, uid: str, data: UpdateUserRequest) -> UserResponse:
        try:
            return await self.user_service.update_by_id(uid, data)
        except ae.NotFoundError as ex:
            logger.error(f'Usuario {uid} no encontrado')
            raise NotFound(ex.message, 'USER_UPDATE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(
                f'Error desconocido al actualizar usuario {uid}: {ex}')
            raise InternalServerError(
                message=f'Error al actualizar usuario {uid}',
                exception_code='USER_UNHANDLED_ERROR'
            )

    async def delete_by_id(self, uid: str) -> None:
        try:
            return await self.user_service.delete_by_id(uid)
        except ae.NotFoundError as ex:
            logger.error(f'Usuario {uid} no encontrado')
            raise NotFound(ex.message, 'USER_DELETE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(
                f'Error desconocido al eliminar usuario {uid}: {ex}')
            raise InternalServerError(
                message=f'Error al eliminar usuario {uid}',
                exception_code='USER_UNHANDLED_ERROR'
            )