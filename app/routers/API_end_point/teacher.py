from fastapi import APIRouter, HTTPException
from app.schemas.schema import  TeacherCreateRequest
from fastapi import APIRouter, HTTPException, status
from app.controllers.teacher_controller import TeacherController
# G:\project\school_management\school_manage_backend\app\controllers\students.py
teacher_router = APIRouter()

@teacher_router.post("/register",
status_code=status.HTTP_201_CREATED
)
def register_teacher(teacher_data: TeacherCreateRequest):
    try:
        response = TeacherController.register_teacher(teacher_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
