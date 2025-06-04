from typing import Annotated
from fastapi import APIRouter, Query, HTTPException, status
from src.schemas.resource_schemas import ResourcePaginatedResponse
from .dependencies import resource_controller

router = APIRouter(
    prefix="/resources",
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
    summary="Listado de recursos paginados",
    description="Obtiene una lista paginada de todos los recursos.",
    response_description="Objeto con la lista de recursos y datos de paginación.",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Bad Request. Revisa los parámetros de paginación."},
    },
)
async def get_paginated(
    page: Annotated[int, Query(ge=1, description="Número de página", example=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100, description="Elementos por página", example=10)] = 10,
) -> ResourcePaginatedResponse:
    try:
        return await resource_controller.get_paginated(page, limit)
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener lista paginada: {ex}",
        )