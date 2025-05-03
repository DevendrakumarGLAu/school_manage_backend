# app/routers/user_router.py
from fastapi import APIRouter, HTTPException
from school.models import User

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = User.objects.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
