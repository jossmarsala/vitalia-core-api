from typing import Annotated

from fastapi import APIRouter, Path, Query, HTTPException, status

from .dependencies import score_controller
from src.schemas.score_schemas import (
    NewScoreRequest,
    UpdateScoreRequest,
    ScoreResponse,
    ScorePaginatedResponse,
)


router = APIRouter(
    prefix="/scores",
    responses={
        400: {"description": "Solicitud incorrecta: parámetros o cuerpo inválido."},
        401: {"description": "No autorizado."},
        403: {"description": "Prohibido."},
        500: {"description": "Error interno del servidor."},
        501: {"description": "No implementado."},
    },
)

@router.get(
    "",
    name="Lista paginada de puntajes",
    description="Devuelve una lista paginada de recursos recomendados.",
    response_description="Lista de resultados y datos de paginación.",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Parámetros de paginación no válidos."},
    },
)
async def get_paginated(
    page: Annotated[int, Query(ge=1, description="Número de página", example=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100, description="Elementos por página", example=10)] = 10,
) -> ScorePaginatedResponse:
    try:
        return await score_controller.get_paginated(page, limit)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar recursos: {ex}",
        )


@router.post(
    "",
    name="Crear nuevo puntaje",
    description="Crea un nuevo puntaje con los datos proporcionados.",
    status_code=status.HTTP_201_CREATED,
    response_description="Puntaje creado correctamente.",
    responses={
        201: {"description": "Puntaje creado correctamente."},
        400: {"description": "Bad Request: Revisa el body request."},
    },
)
async def create(new_score: NewScoreRequest) -> ScoreResponse:
    try:
        return await score_controller.create(new_score)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear puntaje: {ex}",
        )

@router.get(
    "/{score_id}",
    name="Obtener puntaje por ID",
    description="Retorna el puntaje asociado al ID especificado.",
    response_description="Puntaje encontrado.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Puntaje encontrado."},
        404: {"description": "Puntaje no encontrado."},
    },
)
async def get_by_id(
    score_id: Annotated[int, Path(..., ge=1, title="ID del puntaje", description="Identificador único del puntaje")]
) -> ScoreResponse:
    try:
        return await score_controller.get_by_id(score_id)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Puntaje no encontrado: {ex}",
        )


@router.patch(
    "/{score_id}",
    name="Actualizar puntaje por ID",
    description="Actualiza los campos del puntaje identificado por ID.",
    response_description="Puntaje actualizado correctamente.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Puntaje actualizado correctamente."},
        404: {"description": "No se encontró el puntaje para actualizar."},
    },
)
async def update_by_id(
    score_id: Annotated[int, Path(..., ge=1, title="ID del puntaje")],
    score_data: UpdateScoreRequest,
) -> ScoreResponse:
    try:
        return await score_controller.update(score_id, score_data)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error al actualizar puntaje: {ex}",
        )


@router.delete(
    "/{score_id}",
    name="Eliminar puntaje por ID",
    description="Elimina el puntaje identificado por ID.",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Puntaje eliminado correctamente.",
    responses={
        204: {"description": "Puntaje eliminado correctamente."},
        404: {"description": "No se encontró el puntaje para eliminar."},
    },
)
async def delete_by_id(
    score_id: Annotated[int, Path(..., ge=1, title="ID del puntaje")],
) -> None:
    try:
        await score_controller.delete(score_id)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error al eliminar puntaje: {ex}",
        )
    return None