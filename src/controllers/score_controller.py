from src.exceptions.server_exceptions import InternalServerError
from src.schemas.score_schemas import NewScoreRequest, UpdateScoreRequest, ScoreResponse, ScorePaginatedResponse


class ScoreController():
    def __init__(self, score_service):
        self.score_service = score_service

    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        try:
            return await self.score_service.get_paginated(page, limit)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al listar puntaje',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def create(self, data: NewScoreRequest) -> ScoreResponse:
        try:
            return await self.score_service.create(data)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al crear puntaje "{data.name}"',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def get_by_id(self, score_id: int) -> ScoreResponse:
        try:
            return await self.score_service.get_by_id(score_id)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener puntaje #{score_id}',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def update(self, score_id: int, data: UpdateScoreRequest) -> ScoreResponse:
        try:
            return await self.score_service.update(score_id, data)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar puntaje #{score_id}',
                exception_code="SCORE_UNHANDLED_ERROR"
            )

    async def delete(self, score_id: int) -> None:
        try:
            return await self.score_service.delete(score_id)
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar puntaje #{score_id}',
                exception_code="SCORE_UNHANDLED_ERROR"
            )
