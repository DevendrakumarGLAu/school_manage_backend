from django.db import models
from .base import BaseModel
from .user import User

class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    enrollment_number = models.CharField(max_length=50, unique=True)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=5, default='A')

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.enrollment_number}"
    
    class Meta:
        db_table = 'student'
