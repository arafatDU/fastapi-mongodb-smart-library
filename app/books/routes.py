from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.books.dal import BookDAL

router = APIRouter()

@router.post("/")
async def create_book(title: str, author: str, isbn: str, copies: int):
    book_dal = BookDAL(db["books"])
    return await book_dal.create_book(title, author, isbn, copies)

@router.get("/{book_id}")
async def get_book(book_id: str):
    book_dal = BookDAL(db["books"])
    book = await book_dal.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book