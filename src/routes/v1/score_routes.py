from fastapi import APIRouter

router = APIRouter(prefix="/score")

# [GET] /api/v1/score/expenses (obtener listado)
@router.get("")
async def get_paginated():
    return []

@router.post("")
async def create():
    return {}

@router.get("/{score_id}")
async def get_by_id(expense_id: int)
    return {}

@router.patch("/{score_id}")
async def update_by_id(expense_id: int)
    return {}

@router.delete("/{score_id}")
async def delete_by_id(expense_id: int)
    return None