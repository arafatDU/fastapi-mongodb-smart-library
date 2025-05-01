from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.loans.dal import LoanDAL
from bson.errors import InvalidId

router = APIRouter()

@router.post("/")
async def create_loan(user_id: str, book_id: str, issue_date, due_date):
    loan_dal = LoanDAL(db["loans"], db["users"], db["books"])
    try:
        return await loan_dal.create_loan(user_id, book_id, issue_date, due_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.get("/{loan_id}")
async def get_loan(loan_id: str):
    loan_dal = LoanDAL(db["loans"], db["users"], db["books"])
    loan = await loan_dal.get_loan(loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan