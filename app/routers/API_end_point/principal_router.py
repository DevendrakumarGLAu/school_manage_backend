from fastapi import APIRouter, HTTPException, status
from app.schemas.schema import PrincipalCreateRequest
from app.controllers.principal_controller import PrincipalController

principal_router = APIRouter()

@principal_router.post("/register", status_code=status.HTTP_201_CREATED)
def register_principal(principal_data: PrincipalCreateRequest):
    try:
        response = PrincipalController.register_principal(principal_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
