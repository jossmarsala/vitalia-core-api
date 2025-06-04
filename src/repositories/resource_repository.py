from google.cloud.firestore import DocumentSnapshot
from typing import List, Any, Dict, Optional

from .base_repository import FirestoreBaseRepository


class ResourceRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="resources")
    
    async def get_paginated(self, limit: int, start_after_id: Optional[str] = None) -> List[Dict[str, Any]]:
        query = self.collection.order_by("__name__")

        if start_after_id:
            doc_ref = self.collection.document(start_after_id)
            snapshot = doc_ref.get()
            if snapshot.exists:
                query = query.start_after(snapshot)
            else:
                return []
            
        query = query.limit(limit)
        docs = query.stream()

        resources: List[Dict[str, Any]] = []
        async for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            resources.append(data)
        
        return resources