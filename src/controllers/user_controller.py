from src.exceptions.server_exceptions import InternalServerError
from src.schemas.user_schemas import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserPaginatedResponse
)


class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    async def get_paginated(self, page: int, limit: int) -> UserPaginatedResponse:
        try:
            return await self.user_service.get_paginated(page, limit)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al listar usuario',
                exception_code="USER_UNHANDLED_ERROR"
            )

    async def create(self, data: NewUserRequest) -> UserResponse:
        try:
            return await self.user_service.create(data)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al crear usuario "{data.name}"',
                exception_code="USER_UNHANDLED_ERROR"
            )

    async def get_by_id(self, user_id: int) -> UserResponse:
        try:
            return await self.user_service.get_by_id(user_id)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener usuario #{user_id}',
                exception_code="USER_UNHANDLED_ERROR"
            )

    async def update(self, user_id: int, data: UpdateUserRequest) -> UserResponse:
        try:
            return await self.user_service.update(user_id, data)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar usuario #{user_id}',
                exception_code="USER_UNHANDLED_ERROR"
            )

    async def delete(self, user_id: int) -> None:
        try:
            return await self.user_service.delete(user_id)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar usuario #{user_id}',
                exception_code="USER_UNHANDLED_ERROR"
            )
