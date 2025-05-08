from typing import Annotated
from fastapi import APIRouter, Path, HTTPException, status
from src.schemas.user_schemas import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserPaginatedResponse
)

from .dependencies import user_controller

router = APIRouter(
    prefix="/users",
    responses={
        400: {"description": "Solicitud incorrecta."},
        401: {"description": "No autorizado."},
        403: {"description": "Prohibido."},
        500: {"description": "Error interno del servidor."},
    },
)


@router.get(
    "",
    name="Listar usuarios",
    description="Devuelve lista paginada de usuarios.",
    response_description="Lista de usuarios con paginación.",
    status_code=status.HTTP_200_OK
)
async def get_users(
    page: Annotated[int, Path(..., ge=1)] = 1,
    limit: Annotated[int, Path(..., ge=1, le=100)] = 10
) -> UserPaginatedResponse:
    try:
        return await user_controller.get_paginated(page, limit)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar usuarios: {ex}"
        )


@router.post(
    "",
    name="Crear usuario",
    status_code=status.HTTP_201_CREATED,
    response_description="Usuario creado exitosamente."
)
async def create_user(new_user: NewUserRequest) -> UserResponse:
    try:
        return await user_controller.create(new_user)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear usuario: {ex}"
        )


@router.get(
    "/{user_id}",
    name="Obtener usuario por ID",
    status_code=status.HTTP_200_OK
)
async def get_user(
    user_id: Annotated[int, Path(..., ge=1)]
) -> UserResponse:
    try:
        return await user_controller.get_by_id(user_id)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario no encontrado: {ex}"
        )


@router.patch(
    "/{user_id}",
    name="Actualizar usuario",
    status_code=status.HTTP_200_OK
)
async def update_user(
    user_id: Annotated[int, Path(..., ge=1)],
    data: UpdateUserRequest
) -> UserResponse:
    try:
        return await user_controller.update(user_id, data)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error al actualizar usuario: {ex}"
        )


@router.delete(
    "/{user_id}",
    name="Eliminar usuario",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id: Annotated[int, Path(..., ge=1)]
) -> None:
    try:
        await user_controller.delete(user_id)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error al eliminar usuario: {ex}"
        )
    return None
