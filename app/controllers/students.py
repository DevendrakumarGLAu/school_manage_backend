from django.db import transaction
from django.contrib.auth.hashers import make_password
from school.models.user import User
from school.models.student import Student
from app.schemas.schema import StudentCreateRequest,StudentUpdateRequest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
class StudentController:
    def getStudentData():
        return "hello"
    def register_student(student_data: StudentCreateRequest):
        try:
            username = student_data.email
            password = student_data.father_contact
            user = User.objects.create(
                username= username,
                email=student_data.email,
                password=make_password(password),
                first_name=student_data.first_name,
                last_name=student_data.last_name,
                phone=student_data.phone,
                address=student_data.address,
                role='STUDENT'
            )

            student = Student.objects.create(
                user=user,
                enrollment_number=student_data.enrollment_number,
                grade=student_data.grade,
                section=student_data.section,
                date_of_birth=student_data.date_of_birth,
                mother_name=student_data.mother_name,
                mother_contact=student_data.mother_contact,
                father_name=student_data.mother_name,
                father_contact=student_data.father_contact,
                admission_date=student_data.admission_date,
                created_by=user,
                updated_by=user
            )
            return {
                "status":"success",
                "message":"Student registered successfully",
                "student_id":student.id
            }
        except Exception as e:
            # print(f" error in registering students:{str(e)}")
            # raise Exception(f" error in registering students:{str(e)}")
            if 'user_username_key' in str(e):
                return {
                    "status": "failed",
                    "message": "A user with this email/username already exists."
                }

    def update_student(student_data: StudentUpdateRequest):
        try:
            student_id = student_data.id
            try:
                user = User.objects.get(id=student_id, role='STUDENT')
            except ObjectDoesNotExist:
                    raise NotFound(f"Student with ID {student_id} not found.")
            student = user.student_profile
        except Exception as e:
            raise Exception(f" error in registering students:{str(e)}")
