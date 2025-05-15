from fastapi import APIRouter, HTTPException
from app.schemas.schema import StudentCreateRequest

student_router = APIRouter()

@student_router.post("/register-student")
def register_student(student_data: StudentCreateRequest):
    try:
        # For now, simply return the received data
        # You can implement the ORM logic later
        return {"message": "Student registered successfully", "data": student_data.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
