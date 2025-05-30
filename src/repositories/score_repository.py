from .base_repository import FirestoreBaseRepository

class ScoreRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="scores")

    async def list_with_id(self, page: int = 1, limit: int = 10, criteria: dict = None) -> list[dict]:
        docs = await self._filter_documents(criteria)
        start = (page - 1) * limit
        results = []

        for doc in docs[start:start + limit]:
            data = doc.to_dict()
            data["id"] = doc.id
            results.append(data)

        return results

    async def get_by_id(self, doc_id: str) -> dict:
        doc = await self.collection.document(doc_id).get()
        if not doc.exists:
            return None
        data = doc.to_dict()
        data["id"] = doc.id
        return data
