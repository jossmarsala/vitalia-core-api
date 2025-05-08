from src.exceptions.server_exceptions import InternalServerError
from fastapi import HTTPException, status
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
            raise InternalServerError()

    async def create(self, data: NewUserRequest) -> UserResponse:
        try:
            return await self.user_service.create(data)
        except Exception as ex:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creando usuario: {ex}"
            )

    async def get_by_id(self, user_id: int) -> UserResponse:
        try:
            return await self.user_service.get_by_id(user_id)
        except Exception as ex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario no encontrado: {ex}"
            )

    async def update(self, user_id: int, data: UpdateUserRequest) -> UserResponse:
        try:
            return await self.user_service.update(user_id, data)
        except Exception as ex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Error actualizando usuario: {ex}"
            )

    async def delete(self, user_id: int) -> None:
        try:
            return await self.user_service.delete(user_id)
        except Exception as ex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Error eliminando usuario: {ex}"
            )
