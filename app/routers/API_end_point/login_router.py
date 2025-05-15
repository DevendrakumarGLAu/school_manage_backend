# app\routers\API_end_point\login_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from django.contrib.auth import authenticate
from app.jwt_auth import create_access_token
from school.models import User

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

DUMMY_USERS = {
    "admin@example.com": {"password": "admin123", "role": "admin"},
    "teacher@example.com": {"password": "teacher123", "role": "teacher"},
    "student@example.com": {"password": "student123", "role": "student"}
}

@router.post("/login")
def login_user(data: LoginRequest):
    user = DUMMY_USERS.get(data.email)
    if user and user["password"] == data.password:
        # token = f"dummy-token-for-{data.email}"
    # user = authenticate(username=data.email, password=data.password)
    # if not user:
    #     raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"sub": data.email, "role": user["role"]})
        return {
                "status": "success",
                "email": data.email,
                "role": user["role"],
                "token": token
            }
    raise HTTPException(status_code=401, detail="Invalid credentials")
