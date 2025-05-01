from pydantic import BaseModel
from datetime import datetime

class Loan(BaseModel):
    id: str
    user_id: str
    book_id: str
    issue_date: datetime
    due_date: datetime
    return_date: datetime | None
    status: str