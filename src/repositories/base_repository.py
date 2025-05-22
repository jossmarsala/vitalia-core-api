from abc import ABC, abstractmethod
from datetime import datetime

from src.database.database_connection import db

class FirestoreBaseRepository(ABC):
    def __init__(self, collection_name: str):
        self.collection = db.collection(collection_name)

    async def list(self, page=1, limit=10, criteria=None):
        query = self.collection
        if criteria:
            for k,v in criteria.items():
                query = query.where(k, "==", v)
        docs = query.offset((page-1)*limit).limit(limit).stream()
        return [ {**doc.to_dict(), "id": doc.id} for doc in docs ]

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
        doc = self.collection.document(doc_id).get()
        if not doc.exists:
            return None
        return {**doc.to_dict(), "id": doc.id}

    async def create(self, data):
        now = datetime.utcnow().isoformat()
        data["created_at"] = now
        data["updated_at"] = now
        ref = self.collection.document()
        ref.set(data)
        return {**data, "id": ref.id}

    async def update(self, doc_id, data):
        data["updated_at"] = datetime.utcnow().isoformat()
        self.collection.document(doc_id).update(data)
        updated = self.collection.document(doc_id).get().to_dict()
        return {**updated, "id": doc_id}

    async def update_one(self, criteria, data):
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
        self.collection.document(match["id"]).delete()
        return True