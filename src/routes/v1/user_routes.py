from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, status
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
    summary="Listado de usuarios paginados",
    description="Devuelve lista paginada de usuarios.",
    response_description="Lista de usuarios con paginación.",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Parámetros de paginación inválidos."},
    }
)
async def get_users(
    page: Annotated[int, Query(ge=1, description="Número de página", example=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100, description="Cantidad por página", example=10)] = 10
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
    summary="Crear un nuevo usuario",
    description="Crea un nuevo usuario con los datos proporcionados.",
    status_code=status.HTTP_201_CREATED,
    response_description="Usuario creado exitosamente.",
    responses={
        201: {"description": "Usuario creado exitosamente."},
        400: {"description": "Cuerpo de solicitud inválido."},
    }
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
    summary="Obtener usuario por ID",
    description="Obtiene los datos de un usuario dado su ID.",
    status_code=status.HTTP_200_OK,
    response_description="Usuario encontrado.",
    responses={
        200: {"description": "Usuario encontrado."},
        404: {"description": "Usuario no encontrado."},
    }
)
async def get_user(
    user_id: Annotated[int, Path(..., ge=1, title="ID del usuario", description="Identificador único del usuario")]
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
    summary="Actualizar un usuario existente",
    description="Actualiza los datos del usuario identificado por su ID.",
    status_code=status.HTTP_200_OK,
    response_description="Usuario actualizado correctamente.",
    responses={
        200: {"description": "Usuario actualizado correctamente."},
        404: {"description": "Usuario no encontrado para actualización."},
    }
)
async def update_user(
    user_id: Annotated[int, Path(..., ge=1, title="ID del usuario")],
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
    summary="Eliminar un usuario por ID",
    description="Elimina el usuario especificado por su ID.",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Usuario eliminado correctamente.",
    responses={
        204: {"description": "Usuario eliminado correctamente."},
        404: {"description": "Usuario no encontrado para eliminar."},
    }
)
async def delete_user(
    user_id: Annotated[int, Path(..., ge=1, title="ID del usuario")]
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
