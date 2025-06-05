from fastapi import APIRouter

common_router = APIRouter()

from app.routers.API_end_point.login_router import router as login_router
from app.routers.API_end_point.user_router import router as user_router
from app.routers.API_end_point.db_check import router as db_check
from app.routers.API_end_point.students import student_router
from app.routers.API_end_point.teacher import teacher_router

# --------------------auth router --------------------- #
common_router.include_router(login_router, prefix="/auth", tags=["auth"])

# --------------------users router --------------------- #
common_router.include_router(user_router, prefix="/users", tags=["users"])

# --------------------student router --------------------- #
common_router.include_router(db_check, prefix="/db-check", tags=["db_check"])

# --------------------teacher router --------------------- #
common_router.include_router(student_router, prefix="/students", tags=["students"])

# --------------------principle router --------------------- #
common_router.include_router(teacher_router, prefix="/teachers", tags=["teachers"])

# --------------------principle router --------------------- #
from app.routers.API_end_point.principal_router import principal_router
common_router.include_router(principal_router, prefix="/principals", tags=["principals"])


# ---------------------fee router ------------------#
from app.routers.API_end_point.fee_router import fee_router
common_router.include_router(fee_router, prefix="/fees", tags=["fees"])



