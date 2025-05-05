from fastapi import APIRouter

router = APIRouter(prefix="/users")

# [METHOD] /api/v1/users/

@router.get("")
async def get_paginated():
    return []

@router.post("")
async def create():
    return {}

@router.get("/{user_id}")
async def get_by_id(user_id: int)
    return {}

@router.patch("/{user_id}")
async def update_by_id(user_id: int)
    return {}

@router.delete("/{user_id}")
async def delete_by_id(user_id: int)
    return None