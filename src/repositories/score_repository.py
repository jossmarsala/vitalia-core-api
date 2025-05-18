class ScoreRepository():
    
    async def count(self, criteria: dict = {}) -> int:
        pass

    async def get_list(self, page: int, limit: int, criteria: dict = {}) -> list[dict]:
        pass

    async def create(self, data: dict) -> dict:
        pass

    async def get_by_criteria(self, criteria: dict) -> dict | None:
        pass

    async def update_one(self, criteria: dict, data: dict) -> dict | None:
        pass

    async def delete_one(self, criteria: dict) -> bool:
        pass