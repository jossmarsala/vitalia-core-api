from fastapi import APIRouter

router = APIRouter(prefix="/scores")

# [METHOD] /api/v1/scores/

@router.get("")
async def get_paginated():
    return []

@router.post("")
async def create():
    return {}

@router.get("/{score_id}")
async def get_by_id(score_id: int)
    return {}

@router.patch("/{score_id}")
async def update_by_id(score_id: int)
    return {}

@router.delete("/{score_id}")
async def delete_by_id(score_id: int)
    return None