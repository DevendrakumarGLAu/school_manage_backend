from django.db import models
from .base import BaseModel
from .student import Student

class PaymentTransaction(BaseModel):
    student_fee = models.ForeignKey("fee.StudentFee", on_delete=models.CASCADE, related_name="transactions")
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('CASH', 'Cash'), ('ONLINE', 'Online'), ('BANK', 'Bank Transfer')])
    status = models.CharField(max_length=10, choices=[('SUCCESS', 'Success'), ('FAILED', 'Failed')])

    class Meta:
        db_table = 'payment_transaction'
