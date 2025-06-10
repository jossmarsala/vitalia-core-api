from typing import List, Dict, Optional, Any

from .base_repository import FirestoreBaseRepository

class ScoreRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="scores")

    async def get_by_id(self, uid: str) -> dict:
        doc = self.collection.document(uid).get()
        if not doc.exists:
            return None
        data = doc.to_dict()
        data["id"] = doc.id
        return data

    async def count_by_id(self, uid: str) -> int:
        return await self.count(criteria={"uid": uid})
    
    async def get_many(self, page: int, limit: int) -> List[dict]:
        offset = (page - 1) * limit
        docs = list(self.collection.limit(limit).offset(offset).stream())
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]
