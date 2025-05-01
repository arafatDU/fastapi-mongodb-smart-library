from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from bson.errors import InvalidId

class LoanDAL:
    def __init__(self, loan_collection: AsyncIOMotorCollection, user_collection: AsyncIOMotorCollection, book_collection: AsyncIOMotorCollection):
        self.loan_collection = loan_collection
        self.user_collection = user_collection
        self.book_collection = book_collection

    async def create_loan(self, user_id: str, book_id: str, issue_date, due_date) -> dict:
        try:
            user = await self.user_collection.find_one({"_id": ObjectId(user_id)})
        except InvalidId:
            raise ValueError("Invalid user ID")

        if not user:
            raise ValueError("User not found")

        try:
            book = await self.book_collection.find_one({"_id": ObjectId(book_id)})
        except InvalidId:
            raise ValueError("Invalid book ID")

        if not book or book["available_copies"] <= 0:
            raise ValueError("Book not found or no available copies")

        loan = {"user_id": user_id, "book_id": book_id, "issue_date": issue_date, "due_date": due_date, "status": "ACTIVE"}
        result = await self.loan_collection.insert_one(loan)

        await self.book_collection.update_one({"_id": ObjectId(book_id)}, {"$inc": {"available_copies": -1}})

        loan["_id"] = str(result.inserted_id)
        return loan

    async def get_loan(self, loan_id: str) -> dict:
        loan = await self.loan_collection.find_one({"_id": ObjectId(loan_id)})
        if loan:
            loan["_id"] = str(loan["_id"])
        return loan