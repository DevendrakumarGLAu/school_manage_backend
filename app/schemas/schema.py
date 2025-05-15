from pydantic import BaseModel

class StudentCreateRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    age: int
    password: str