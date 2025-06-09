from typing import Annotated

from fastapi import APIRouter, Query, Path, HTTPException, status, Depends

from .dependencies import user_controller
from src.schemas.user_schemas import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserPaginatedResponse
)


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
    name="Lista paginada de usuarios",
    description="Devuelve lista paginada de usuarios.",
    response_description="Lista de usuarios con paginación.",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Parámetros de paginación inválidos."},
    }
)
async def get_paginated(
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
    name="Crear nuevo usuario",
    description="Crea un nuevo usuario con los datos proporcionados.",
    status_code=status.HTTP_201_CREATED,
    response_description="Usuario creado exitosamente.",
    responses={
        201: {"description": "Usuario creado exitosamente."},
        400: {"description": "Bad Request: Revisa el body request."},
    }
)
async def create(new_user: NewUserRequest) -> UserResponse:
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
    description="Obtiene los datos del usuario asociado a su ID.",
    status_code=status.HTTP_200_OK,
    response_description="Usuario encontrado.",
    responses={
        200: {"description": "Usuario encontrado."},
        404: {"description": "Usuario no encontrado."},
    }
)
async def gey_by_id(
    user_id: Annotated[str, Path(title="ID del usuario")],
) -> UserResponse:
    try:
        return await user_controller.get_by_id(user_id)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario no encontrado: {ex}",
        )


@router.patch(
    "/{user_id}",
    name="Actualizar usuario por su ID",
    description="Actualiza los datos del usuario autenticado en base a su token.",
    status_code=status.HTTP_200_OK,
    response_description="Usuario actualizado correctamente.",
    responses={
        200: {"description": "Usuario actualizado correctamente."},
        404: {"description": "No se encontró el usuario para actualizar."},
    }
)
async def update_by_id(
    user_id: Annotated[str, Path(title="ID del usuario")],
    user_data: UpdateUserRequest,
) -> UserResponse:
    try:
        return await user_controller.update_by_id(user_id, user_data)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error al actualizar usuario: {ex}",
        )


@router.delete(
    "/{user_id}",
    name="Eliminar usuario por ID",
    description="Elimina un usuario existente.",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Usuario eliminado correctamente.",
    responses={
        204: {"description": "Usuario eliminado correctamente."},
        404: {"description": "No se encontró el usuario para eliminar."},
    }
)
async def delete_by_id(
    user_id: Annotated[str, Path(title="ID del usuario")],
) -> None:
    try:
        await user_controller.delete_by_id(user_id)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error al eliminar usuario: {ex}",
        )
    return None