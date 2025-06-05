from django.db import transaction
from django.contrib.auth.hashers import make_password
from school.models.user import User
from school.models.teacher import Teacher
from app.schemas.schema import TeacherCreateRequest

class TeacherController:

    @staticmethod
    def register_teacher(teacher_data: TeacherCreateRequest):
        try:
            with transaction.atomic():
                # Create User
                user = User.objects.create(
                    username=teacher_data.username,
                    email=teacher_data.email,
                    password=make_password(teacher_data.password),
                    first_name=teacher_data.first_name,
                    last_name=teacher_data.last_name,
                    phone=teacher_data.phone,
                    address=teacher_data.address,
                    role='TEACHER'
                )

                teacher = Teacher.objects.create(
                    user=user,
                    subject=teacher_data.subject,
                    qualification=teacher_data.qualification,
                    created_by=user,
                    updated_by=user
                )

                return {
                    "status": "success",
                    "message": "Teacher registered successfully",
                    "teacher_id": teacher.id
                }

        except Exception as e:
            raise Exception(f"Error in registering teacher: {str(e)}")
