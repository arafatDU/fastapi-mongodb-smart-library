from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.users.dal import UserDAL

router = APIRouter()

@router.post("/")
async def create_user(name: str, email: str, role: str):
    user_dal = UserDAL(db["users"])
    return await user_dal.create_user(name, email, role)

@router.get("/{user_id}")
async def get_user(user_id: str):
    user_dal = UserDAL(db["users"])
    user = await user_dal.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user