from typing import List, Dict, Any, Optional

from .base_repository import FirestoreBaseRepository

class UserRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="users")

    def get_paginated(self, page: int = 1, limit: int = 10, criteria: Optional[dict] = None) -> List[Dict[str, Any]]:
        docs = self.collection.stream() 
        all_users: List[Dict[str, Any]] = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            all_users.append(data)

        if criteria:
            filtered = []
            for r in all_users:
                cumple = True
                for k, v in criteria.items():
                    if r.get(k) != v:
                        cumple = False
                        break
                if cumple:
                    filtered.append(r)
            all_users = filtered

        all_users.sort(key=lambda x: x["id"])

        start = (page - 1) * limit
        end = start + limit
        return all_users[start:end]

    async def get_by_id(self, uid: str) -> dict:
        doc = self.collection.document(uid).get()
        if not doc.exists:
            return None
        data = doc.to_dict()
        data["id"] = doc.id
        return data
    
    def count(self, criteria: Optional[dict] = None) -> int:
        docs = self.collection.stream()
        all_users: List[Dict[str, Any]] = [doc.to_dict() for doc in docs]
        if criteria:
            all_users = [r for r in all_users if all(r.get(k) == v for k, v in criteria.items())]
        return len(all_users)
    
    async def count_by_id(self, uid: str) -> int:
        return await self.count(criteria={"uid": uid})
    
    async def get_many(self, page: int, limit: int) -> List[dict]:
        offset = (page - 1) * limit
        docs = list(self.collection.limit(limit).offset(offset).stream())
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]
