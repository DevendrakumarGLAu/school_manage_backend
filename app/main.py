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
from fastapi.middleware.cors import CORSMiddleware
from app.routers.common_router import common_router 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(common_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)