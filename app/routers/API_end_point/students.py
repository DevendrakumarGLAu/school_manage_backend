from fastapi import APIRouter, HTTPException
from app.schemas.schema import StudentCreateRequest
from fastapi import APIRouter, HTTPException, status
from app.controllers.students import StudentController
# G:\project\school_management\school_manage_backend\app\controllers\students.py
student_router = APIRouter()

@student_router.get("/getStudentData", status_code=status.HTTP_201_CREATED)
def getStudentData():
    response = StudentController.getStudentData()
    return response

@student_router.post("/register",
status_code=status.HTTP_201_CREATED
)
def register_student(student_data: StudentCreateRequest):
    try:
        response = StudentController.register_student(student_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
