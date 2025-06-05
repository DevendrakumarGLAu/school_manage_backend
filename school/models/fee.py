from django.db import models
from .base import BaseModel
from .student import Student

class FeeCategory(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'fee_category'

    def __str__(self):
        return self.name

class FeeStructure(BaseModel):
    category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE, related_name="fee_structures")
    grade = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'fee_structure'

class StudentFee(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_fees")
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE, related_name="student_fees")
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('PAID', 'Paid'), ('UNPAID', 'Unpaid'), ('PARTIAL', 'Partial')])
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'student_fee'
