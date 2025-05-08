from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, status
from src.schemas.score_schemas import (
    NewScoreRequest,
    UpdateScoreRequest,
    ScoreResponse,
    ScorePaginatedResponse,
)
from .dependencies import score_controller

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
    name="Lista paginada",
    description="Obtiene una lista paginada de recursos recomendados.",
    response_description="Objeto con la lista de resultados y datos de paginación.",
    status_code=status.HTTP_200_OK,
)
async def get_paginated(
    page: Annotated[int, Query(1, ge=1)] = 1,
    limit: Annotated[int, Query(10, ge=1, le=100)] = 10,
) -> ScorePaginatedResponse:
    """
    Lista paginada de ScoreResponse.
    """
    try:
        return await score_controller.get_paginated(page, limit)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener lista paginada: {ex}",
        )

@router.post(
    "",
    name="Crear nuevo puntaje",
    status_code=status.HTTP_201_CREATED,
    response_description="Puntaje creado correctamente.",
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
    response_description="Puntaje encontrado.",
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    score_id: Annotated[int, Path(..., ge=1, title="ID del puntaje")],
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
    response_description="Puntaje actualizado correctamente.",
    status_code=status.HTTP_200_OK,
)
async def update_by_id(
    score_id: Annotated[int, Path(..., ge=1, title="ID del puntaje")],
    data: UpdateScoreRequest,
) -> ScoreResponse:
    try:
        return await score_controller.update(score_id, data)
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
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Puntaje eliminado correctamente.",
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
