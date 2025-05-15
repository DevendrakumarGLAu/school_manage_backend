from fastapi import APIRouter

common_router = APIRouter()

from app.routers.API_end_point.login_router import router as login_router
from app.routers.API_end_point.user_router import router as user_router
from app.routers.API_end_point.db_check import router as db_check
from app.routers.API_end_point.students import student_router

common_router.include_router(login_router, prefix="/auth", tags=["auth"])
common_router.include_router(user_router, prefix="/users", tags=["users"])
common_router.include_router(db_check, prefix="/db-check", tags=["db_check"])
common_router.include_router(student_router, prefix="/students", tags=["students"])
