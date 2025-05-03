# app\routers\API_end_point\login_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from django.contrib.auth import authenticate
from app.jwt_auth import create_access_token
from school.models import User

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login_user(data: LoginRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username, "role": user.role})
    return {
        "access_token": token,
        "role": user.role,
        "username": user.username
    }
