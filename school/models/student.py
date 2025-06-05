from django.db import models
from .base import BaseModel
from .user import User

class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    enrollment_number = models.CharField(max_length=50, unique=True)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=5, default='A')
    date_of_birth = models.DateField(null = True, blank = True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_contact = models.CharField(max_length=15, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    father_contact = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.enrollment_number}"
    
    class Meta:
        db_table = 'student'
