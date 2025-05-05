from fastapi import APIRouter

router = APIRouter(prefix="/scores")

# [METHOD] /api/v1/scores/

@router.get(
    "", 
    name="Lista paginada", 
    description="Lista de recursos recomendados paginada",
    response_description="Retorna un objeto con la lista de resultados y la información de la paginación.",
    status_code=200,
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
        "total_items": 0,
        "items_per_page": 10,
        "has_previous": False,
        "has_next": False
        }
    }

@router.post("")
async def create():
    return {}

@router.get("/{score_id}")
async def get_by_id(score_id: int):
    return {}

@router.patch("/{score_id}")
async def update_by_id(score_id: int):
    return {}

@router.delete("/{score_id}")
async def delete_by_id(score_id: int):
    return None