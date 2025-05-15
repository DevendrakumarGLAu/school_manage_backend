from fastapi import APIRouter
from django.db import connection

router = APIRouter()

@router.get("/db-check")
def db_check():
    try:
        connection.ensure_connection()
        return {"status": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
