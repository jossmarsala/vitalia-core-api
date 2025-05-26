from .base_repository import FirestoreBaseRepository

class UserRepository(FirestoreBaseRepository):
    def __init__(self):
        super().__init__(collection_name="users")

    async def get_by_user_uid(self, uid: str, page: int = 1, limit: int = 50) -> list[dict]:
        return await self.list(page=page, limit=limit, criteria={"uid": uid})

    async def count_by_user_uid(self, uid: str) -> int:
        return await self.count(criteria={"uid": uid})
