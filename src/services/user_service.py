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
        logger.debug(f'Obteniendo recursos paginados. Página: {page}, Límite: {limit}')

        raw_users = self.user_repo.get_paginated(page=page, limit=limit)
        users: List[UserResponse] = []
        for idx, r in enumerate(raw_users):
            try:
                validated = UserResponse.model_validate(r)
                users.append(validated)
            except Exception as e:
                logger.error(f"No se pudo validar el recurso #{idx}: {r}")
                logger.exception(e)

        total_count = self.user_repo.count()

        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages
        if page > total_pages:
            raise ae.NotFoundError(f'La página {page} no existe')

        has_previous = page > 1
        has_next = page < total_pages

        logger.debug(f'Usuarios validados: {len(users)} de {total_count} totales.')
        return UserPaginatedResponse(
            results=users,
            meta={
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "items_per_page": limit,
                "has_previous_page": has_previous,
                "has_next_page": has_next
            }
        )


    async def create(self, data: NewUserRequest) -> UserResponse:
        from src.services.score_service import ScoreService
        score_service = ScoreService()

        raw_user = await self.user_repo.create(data.model_dump(mode='json'))
        uid = raw_user["uid"]
        await score_service.match_and_create(uid, raw_user)
        return UserResponse.model_validate(raw_user)

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
