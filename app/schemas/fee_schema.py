from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class FeeCategoryRequest(BaseModel):
    name: str
    description: Optional[str] = None

class FeeStructureRequest(BaseModel):
    category_id: int
    grade: str
    amount: float

class StudentFeeRequest(BaseModel):
    student_id: int
    fee_structure_id: int
    due_date: date

class PaymentRequest(BaseModel):
    student_fee_id: int
    amount: float
    payment_method: str
