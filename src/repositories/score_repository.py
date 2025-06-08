from typing import List, Dict, Optional, Any

from .base_repository import FirestoreBaseRepository

class ScoreRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="scores")

    def get_paginated(self, page: int = 1, limit: int = 10, criteria: Optional[dict] = None) -> List[Dict[str, Any]]:
        docs = self.collection.stream() 
        all_scores: List[Dict[str, Any]] = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            all_scores.append(data)

        if criteria:
            filtered = []
            for r in all_scores:
                cumple = True
                for k, v in criteria.items():
                    if r.get(k) != v:
                        cumple = False
                        break
                if cumple:
                    filtered.append(r)
            all_scores = filtered

        all_scores.sort(key=lambda x: x["id"])

        start = (page - 1) * limit
        end = start + limit
        return all_scores[start:end]

    def count(self, criteria: Optional[dict] = None) -> int:
        docs = self.collection.stream()
        all_scores: List[Dict[str, Any]] = [doc.to_dict() for doc in docs]
        if criteria:
            all_scores = [r for r in all_scores if all(r.get(k) == v for k, v in criteria.items())]
        return len(all_scores)

    def list_with_id(self, page: int = 1, limit: int = 10, criteria: dict = None) -> list[dict]:
        docs = self._filter_documents(criteria)
        start = (page - 1) * limit
        results = []

        for doc in docs[start:start + limit]:
            data = doc.to_dict()
            data["id"] = doc.id
            results.append(data)

        return results

    def get_by_id(self, doc_id: str) -> dict:
        doc = self.collection.document(doc_id).get()
        if not doc.exists:
            return None
        data = doc.to_dict()
        data["id"] = doc.id
        return data
    
    def get_many(self, page: int, limit: int) -> List[dict]:
        offset = (page - 1) * limit
        docs = list(self.collection.limit(limit).offset(offset).stream())
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]
