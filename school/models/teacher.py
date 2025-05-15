from django.db import models
from .base import BaseModel
from .user import User

class Teacher(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.subject}"

    class Meta:
        db_table = 'teacher'
