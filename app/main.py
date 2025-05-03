import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Initialize Django
django.setup()

# Import FastAPI and other dependencies
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from django.contrib.auth import authenticate
from school.models import User
from .jwt_auth import create_access_token

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
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

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Management API"}
