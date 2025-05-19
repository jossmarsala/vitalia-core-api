from abc import ABC, abstractmethod
from typing import Dict, List, Any

class BaseRepository(ABC):
    async def count(self, criteria: dict = {}) -> int:
        data = await self._read_all()
        if criteria:
            data = [item for item in data if ]

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

    @abstractmethod
    async def _read_all(self) -> List[Dict[str, Any]]:
        pass