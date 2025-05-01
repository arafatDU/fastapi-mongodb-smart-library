from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

class BookDAL:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_book(self, title: str, author: str, isbn: str, copies: int) -> dict:
        book = {"title": title, "author": author, "isbn": isbn, "copies": copies, "available_copies": copies}
        result = await self.collection.insert_one(book)
        book["_id"] = str(result.inserted_id)
        return book

    async def get_book(self, book_id: str) -> dict:
        book = await self.collection.find_one({"_id": ObjectId(book_id)})
        if book:
            book["_id"] = str(book["_id"])
        return book