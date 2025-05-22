import asyncio
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
        users, total_count = await asyncio.gather(
            self.__get_user_list(page, limit),
            self.__count()
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')

        logger.debug(f'Usuarios obtenidos: {len(users)}')
        return UserPaginatedResponse(
            results=users,
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
        logger.debug(f'Usuario creado: {raw}')
        return UserResponse.model_validate(raw)

    async def get_by_uid(self, uid: str) -> UserResponse:
        logger.debug(f'Obteniendo usuario por UID: {uid}')
        raw = await self.user_repo.get_one_by_criteria({'uid': uid})
        if raw is None:
            raise ae.NotFoundError(f"El usuario con UID '{uid}' no existe")
        return UserResponse.model_validate(raw)

    async def update(self, uid: str, data: UpdateUserRequest) -> UserResponse:
        logger.debug(f'Actualizando usuario {uid} con datos: {data}')
        raw = await self.user_repo.update_one(
            {'uid': uid},
            data.model_dump(mode='json', exclude_unset=True)
        )
        if raw is None:
            raise ae.NotFoundError(f"El usuario con UID '{uid}' no existe")
        return UserResponse.model_validate(raw)

    async def delete(self, uid: str) -> None:
        logger.debug(f'Eliminando usuario {uid}')
        deleted = await self.user_repo.delete_one({'uid': uid})
        if not deleted:
            raise ae.NotFoundError(f"El usuario con UID '{uid}' no existe")
        return None

    async def __count(self) -> int:
        return await self.user_repo.count()

    async def __get_user_list(self, page: int, limit: int) -> List[UserResponse]:
        raw_users = await self.user_repo.get_many(page, limit)
        return [UserResponse.model_validate(u) for u in raw_users]
