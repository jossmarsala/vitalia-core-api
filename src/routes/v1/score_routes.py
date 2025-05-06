from fastapi import APIRouter

router = APIRouter(
    prefix="/scores",
    responses={
        400: {"description": "Bad Request: Revisa la info del cuerpo y/o parámetros."},
        401: {"description": "Unauthorized: Credenciales inválidas o no enviadas."},
        403: {"description": "Forbidden: No tienes acceso a este recurso."},
        500: {"description": "Internal Server Error: Error del servidor no manejado, contacte al sysadmin."},
        501: {"description": "Not Implemented: Esta función no está disponible aún."}
    }
)

# [METHOD] /api/v1/scores/


@router.get(
    "",
    name="Lista paginada",
    description="Lista de recursos recomendados paginada",
    response_description="Retorna un objeto con la lista de resultados y la información de la paginación.",
    status_code=200,
    responses={
        400: {"description": "Bad Request: Revisa los parámetros de paginación o filtrado."}
    }
)
async def get_paginated():
    # TODO: Implementar paginación
    # TODO: Implementar filtros
    # TODO: Implementar tipo de respuesta
    return {
        "results": [],
        "meta": {
            "current_page": 1,
            "total_pages": 1,
            "total_items": 1,
            "items_per_page": 10,
            "has_previous": False,
            "has_next": False
        }
    }


@router.post(
    "",
    name="Crear nuevo puntaje",
    status_code=201,
    responses={
        201: {"description": "Nuevo puntaje creado."},
        400: {"description": "Revisa el body request."}
    }
)
async def create():
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
        name="Obtener puntajes por ID",
        responses={
            200: {"description": "Puntaje encontrado."}
            404: {"description": "Puntaje no encontrado."}
        }
)
async def get_by_id(score_id: int):
    # TODO: Implementar búsqueda por ID
    return {
        "id": 1,
        "planes_alimenticios": [],
        "rutinas": [],
        "articulos": [],
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.patch(
        "/{score_id}",
        name="Actualizar datos de puntaje por id",
        responses={
            200: {"description": "Puntaje actualizado."}
            404: {"description": "Puntaje a actualizar no encontrado."}
        }
)
async def update_by_id(score_id: int):
    # TODO: Implementar la actualización por id (campos todos opcionales)
    return {
        "id": 1,
        "planes_alimenticios": [],
        "rutinas": [],
        "articulos": [],
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.delete(
        "/{score_id}",
        name="Eliminar puntaje por ID",
        status_code= 204,
        responses={
            200: {"description": "Puntaje eliminado."}
            404: {"description": "Puntaje a borrar no encontrado."}
        }
)
async def delete_by_id(score_id: int) -> None:
    # TODO: Implementar borrado por id
    return None
