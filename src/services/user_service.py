import logging
from typing import List

from src.exceptions import app_exceptions as ae
from src.repositories.user_repository import UserRepository
from src.schemas.user_schemas import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserPaginatedResponse
)

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo

    async def get_paginated(self, page: int, limit: int) -> UserPaginatedResponse:
        logger.debug(f'Obteniendo usuarios paginados. Página: {page}, Límite: {limit}')
        raw_users = await self.user_repo.get_paginated(page=page, limit=limit)

        results = [UserResponse.model_validate(user_data) for user_data in raw_users]

        total_count = await self.user_repo.count()
        total_pages = max((total_count // limit) + (1 if total_count % limit else 0), 1)

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')

        return UserPaginatedResponse(
            results=results,
            meta={
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "items_per_page": limit,
                "has_previous_page": page > 1,
                "has_next_page": page < total_pages
            }
        )

    async def create(self, data: NewUserRequest) -> UserResponse:
        logger.debug(f'Creando usuario: {data}')
        raw = await self.user_repo.create(data.model_dump(mode='json'))
        return UserResponse.model_validate(raw)

    async def get_by_id(self, uid: str) -> UserResponse:
        logger.debug(f'Obteniendo usuario por ID: {uid}')
        raw = await self.user_repo.get_by_id(uid)
        if raw is None:
            raise ae.NotFoundError(f"El usuario '{uid}' no existe")
        return UserResponse.model_validate(raw)

    async def update_by_id(self, uid: str, data: UpdateUserRequest) -> UserResponse:
        logger.debug(f'Actualizando usuario {uid} con datos: {data}')
        payload = data.model_dump(mode='json', exclude_unset=True)

        def sanitize_list_field(field):
            if isinstance(field, list):
                return [str(item) if not isinstance(item, str) else item for item in field]
            return []

        for key in ["obstacles", "restrictions", "wellbeingGoals"]:
            if key in payload:
                payload[key] = sanitize_list_field(payload[key])

        raw = await self.user_repo.update(doc_id=uid, data=payload)

        if raw is None:
            raise ae.NotFoundError(f"El usuario con ID '{uid}' no existe")
        return UserResponse.model_validate(raw)

    async def delete_by_id(self, uid: str) -> None:
        logger.debug(f'Eliminando usuario {uid}')
        deleted = await self.user_repo.delete(uid)
        if not deleted:
            raise ae.NotFoundError(f"El usuario con ID '{uid}' no existe")
        return None
