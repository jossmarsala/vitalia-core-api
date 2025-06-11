from typing import List, Dict, Any, Optional

from .base_repository import FirestoreBaseRepository

class ResourceRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="resources")

    def get_paginated(self, page: int = 1, limit: int = 10, criteria: Optional[dict] = None) -> List[Dict[str, Any]]:
        docs = self.collection.stream() 
        all_resources: List[Dict[str, Any]] = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            all_resources.append(data)

        if criteria:
            filtered = []
            for r in all_resources:
                cumple = True
                for k, v in criteria.items():
                    if r.get(k) != v:
                        cumple = False
                        break
                if cumple:
                    filtered.append(r)
            all_resources = filtered

        all_resources.sort(key=lambda x: x["id"])

        start = (page - 1) * limit
        end = start + limit
        return all_resources[start:end]

    def count(self, criteria: Optional[dict] = None) -> int:
        docs = self.collection.stream()
        all_resources: List[Dict[str, Any]] = [doc.to_dict() for doc in docs]
        if criteria:
            all_resources = [r for r in all_resources if all(r.get(k) == v for k, v in criteria.items())]
        return len(all_resources)
    
    def get_all(self):
        docs = self.collection.stream()
        return [doc.to_dict() | {"id": doc.id} for doc in docs]