from fastapi import APIRouter

common_router = APIRouter()

from app.routers.API_end_point.login_router import router as login_router
from app.routers.API_end_point.user_router import router as user_router


common_router.include_router(login_router, prefix="/auth", tags=["auth"])
common_router.include_router(user_router, prefix="/users", tags=["users"])