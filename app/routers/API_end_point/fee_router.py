from fastapi import APIRouter, HTTPException
from app.schemas.fee_schema import FeeCategoryRequest, FeeStructureRequest, StudentFeeRequest
from app.controllers.fee_controller import FeeController

fee_router = APIRouter()

@fee_router.post("/create-category")
def create_fee_category(fee_data: FeeCategoryRequest):
    try:
        return FeeController.create_fee_category(fee_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@fee_router.post("/create-structure")
def create_fee_structure(fee_data: FeeStructureRequest):
    try:
        return FeeController.create_fee_structure(fee_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@fee_router.post("/assign-fee")
def assign_fee_to_student(fee_data: StudentFeeRequest):
    try:
        return FeeController.assign_fee_to_student(fee_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
