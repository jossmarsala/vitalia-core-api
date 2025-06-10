from abc import ABC
from datetime import datetime

from src.database.database_connection import db

class FirestoreBaseRepository(ABC):
    def __init__(self, collection_name: str):
        self.collection = db.collection(collection_name)

    async def list(self, limit=10, start_after=None, criteria=None, order_by="__name__"):
        query = self.collection
        if criteria:
            for k,v in criteria.items():
                query = query.where(k, "==", v)
        
        query = query.order_by(order_by)

        if start_after:
            last_doc = await self.collection.document(start_after).get()
            if last_doc.exists:
                query = query.start_after(last_doc)
            else:
                raise ValueError(f"Documento con ID '{start_after}' no existe")

        docs= query.limit(limit).stream()
        results = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            results.append(data)

        return results

    async def count(self, criteria=None):
        query = self.collection

        if criteria:
            for k,v in criteria.items():
                query = query.where(k, "==", v)

        count = 0
        for _ in query.stream():
            count += 1
        return count

    async def get_one_by_criteria(self, criteria):
        query = self.collection
        for k,v in criteria.items():
            query = query.where(k, "==", v)
            
        query = query.limit(1)
        docs = query.stream()
        for doc in docs:
            return {**doc.to_dict(), "id": doc.id}
        return None

    async def get_by_id(self, doc_id):
        doc = await self.collection.document(doc_id).get()
        if not doc.exists:
            return None
        return {**doc.to_dict(), "id": doc.id}

    async def create(self, data: dict) -> dict:
        now = datetime.utcnow().isoformat()
        data["createdAt"] = now
        data["updatedAt"] = now
        ref = self.collection.document()
        ref.set(data)
        return {**data, "uid": ref.id}

    async def update(self, doc_id, data):
        data["updatedAt"] = datetime.utcnow().isoformat()
        self.collection.document(doc_id).update(data)
        updated_doc = self.collection.document(doc_id).get()
        updated = updated_doc.to_dict()
        return {**updated, "id": doc_id}

    async def update_one(self, criteria: dict, data: dict):
        match = await self.get_one_by_criteria(criteria)
        if not match:
            return None
        doc_id = match["id"]
        return await self.update(doc_id, data)

    async def delete(self, doc_id):
        self.collection.document(doc_id).delete()
        return True

    async def delete_one(self, criteria):
        match = await self.get_one_by_criteria(criteria)
        if not match:
            return False
        await self.collection.document(match["id"]).delete()
        return True