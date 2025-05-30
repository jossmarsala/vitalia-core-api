from .base_repository import FirestoreBaseRepository
from typing import List, Any, Dict

class ResourceRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="resources")
    
    async def get_all(self) -> List[Dict[str, Any]]:
        docs = self.collection.stream()
        resources: List[Dict[str, Any]] = []
        async for doc in docs:
            resources.append(doc.to_dict())
        return resources