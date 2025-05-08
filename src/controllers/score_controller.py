from src.schemas.score_schemas import NewScoreRequest, UpdateScoreRequest, ScoreResponse, ScorePaginatedResponse

class ScoreController():
    def __init__(self, score_service):
        self.score_service = score_service

    async def get_paginated(self, page: int, limit: int) -> ScorePaginatedResponse:
        return await self.score_service.get_paginated(page, limit)

    async def create(self) -> ScoreResponse:
        pass

    async def get_by_id(self) -> ScoreResponse:
        pass

    async def update(self) -> ScoreResponse:
        pass

    async def delete(self) -> None:
        pass