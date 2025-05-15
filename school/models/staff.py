from django.db import models
from .base import BaseModel
from .user import User

class Staff(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_profile")
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"

    class Meta:
        db_table = 'staff'