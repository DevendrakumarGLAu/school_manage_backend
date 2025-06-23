from typing import Optional 
from pydantic import BaseModel, EmailStr 
from datetime import date

class StudentCreateRequest(BaseModel):
    email: EmailStr
    # password: str
    first_name: str
    last_name: str
    phone: Optional[str] = None
    address: Optional[str] = None
    enrollment_number: str
    grade: str
    section: str
    date_of_birth: Optional[date] = None
    mother_name: Optional[str] = None
    father_name: Optional[str] = None
    mother_contact: Optional[str] = None
    father_contact: Optional[str] = None
    admission_date: Optional[date] = None

class StudentUpdateRequest(BaseModel):
    id : int = 0
    username: Optional[str] = None 
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None 
    enrollment_number: Optional[str] = None
    grade: Optional[str] = None
    section: Optional[str] = None
    date_of_birth: Optional[date] = None
    mother_name: Optional[str] = None
    father_name: Optional[str] = None
    mother_contact: Optional[str] = None
    father_contact: Optional[str] = None
    admission_date: Optional[date] = None


class TeacherCreateRequest(BaseModel):
    username:str
    email: EmailStr
    password:str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    subject: str
    qualification: str

class PrincipalCreateRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    qualification: Optional[str] = None