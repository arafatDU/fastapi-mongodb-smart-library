from pydantic import BaseModel

class Book(BaseModel):
    id: str
    title: str
    author: str
    isbn: str
    copies: int
    available_copies: int