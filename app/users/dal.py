from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class UserDAL:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_user(self, name: str, email: str, role: str) -> dict:
        user = {"name": name, "email": email, "role": role}
        result = await self.collection.insert_one(user)
        user["_id"] = str(result.inserted_id)
        return user

    async def get_user(self, user_id: str) -> dict:
        user = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["_id"] = str(user["_id"])
        return user