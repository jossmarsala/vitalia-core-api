from typing import Annotated

from fastapi import APIRouter, Path, Query

from src.schemas.score_schemas import NewScoreRequest, UpdateScoreRequest

router = APIRouter(
    prefix="/scores",
    responses={
        400: {"description": "Solicitud incorrecta: revisa el cuerpo o los parámetros."},
        401: {"description": "No autorizado: credenciales inválidas o no proporcionadas."},
        403: {"description": "Prohibido: no tienes permisos para acceder a este recurso."},
        500: {"description": "Error interno del servidor: contacte al administrador del sistema."},
        501: {"description": "No implementado: esta funcionalidad aún no está disponible."}
    }
)


@router.get(
    "",
    name="Lista paginada",
    description="Obtiene una lista paginada de recursos recomendados.",
    response_description="Objeto con la lista de resultados y datos de paginación.",
    status_code=200,
    responses={
        400: {"description": "Solicitud incorrecta: revisa los parámetros de paginación o filtrado."}
    }
)
async def get_paginated(page: Annotated[int, Query(ge=1)] = 1, limit: Annotated[int, Query(ge=1, le=100)] = 10):
    # TODO: Implementar paginación
    # TODO: Implementar filtros
    # TODO: Definir tipo de respuesta
    return {
        "results": [],
        "meta": {
            "current_page": page,
            "total_pages": 1,
            "total_items": 1,
            "items_per_page": limit,
            "has_previous": False,
            "has_next": False
        }
    }


@router.post(
    "",
    name="Crear nuevo puntaje",
    status_code=201,
    responses={
        201: {"description": "Puntaje creado correctamente."},
        400: {"description": "Solicitud incorrecta: revisa el cuerpo de la petición."}
    }
)
async def create(new_score: NewScoreRequest):
    # TODO: Recibir los datos para crear el puntaje
    return {
        "id": 1,
        "planes_alimenticios": [],
        "rutinas": [],
        "articulos": [],
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.get(
    "/{score_id}",
    name="Obtener puntaje por ID",
    responses={
        200: {"description": "Puntaje encontrado."},
        404: {"description": "Puntaje no encontrado."}
    }
)
async def get_by_id(
    score_id: Annotated[int, Path(ge=1, description="ID del puntaje a buscar",
    title="ID del puntaje")], score_data: UpdateScoreRequest
):
    # TODO: Implementar búsqueda por ID
    return {
        "id": score_id,
        "planes_alimenticios": [],
        "rutinas": [],
        "articulos": [],
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.patch(
    "/{score_id}",
    name="Actualizar puntaje por ID",
    responses={
        200: {"description": "Puntaje actualizado correctamente."},
        404: {"description": "Puntaje no encontrado para actualizar."}
    }
)
async def update_by_id(score_id: Annotated[int, Path(ge=1, description="ID del puntaje a buscar", title="ID del puntaje")]):
    # TODO: Implementar actualización por ID (campos opcionales)
    return {
        "id": score_id,
        "planes_alimenticios": [],
        "rutinas": [],
        "articulos": [],
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.delete(
    "/{score_id}",
    name="Eliminar puntaje por ID",
    status_code=204,
    responses={
        204: {"description": "Puntaje eliminado correctamente."},
        404: {"description": "Puntaje no encontrado para eliminar."}
    }
)
async def delete_by_id(score_id: Annotated[int, Path(ge=1, description="ID del puntaje a buscar", title="ID del puntaje")]) -> None:
    # TODO: Implementar borrado por ID
    return None
