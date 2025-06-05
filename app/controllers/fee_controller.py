from school.models.fee import FeeCategory, FeeStructure, StudentFee
from app.schemas.fee_schema import FeeCategoryRequest, FeeStructureRequest, StudentFeeRequest

class FeeController:

    @staticmethod
    def create_fee_category(fee_data: FeeCategoryRequest):
        try:
            category = FeeCategory.objects.create(
                name=fee_data.name,
                description=fee_data.description
            )
            return {"status": "success", "fee_category_id": category.id}
        except Exception as e:
            raise Exception(f"Error in creating fee category: {str(e)}")

    @staticmethod
    def create_fee_structure(fee_data: FeeStructureRequest):
        try:
            structure = FeeStructure.objects.create(
                category_id=fee_data.category_id,
                grade=fee_data.grade,
                amount=fee_data.amount
            )
            return {"status": "success", "fee_structure_id": structure.id}
        except Exception as e:
            raise Exception(f"Error in creating fee structure: {str(e)}")

    @staticmethod
    def assign_fee_to_student(fee_data: StudentFeeRequest):
        try:
            student_fee = StudentFee.objects.create(
                student_id=fee_data.student_id,
                fee_structure_id=fee_data.fee_structure_id,
                due_date=fee_data.due_date,
                status='UNPAID'
            )
            return {"status": "success", "student_fee_id": student_fee.id}
        except Exception as e:
            raise Exception(f"Error in assigning fee: {str(e)}")
