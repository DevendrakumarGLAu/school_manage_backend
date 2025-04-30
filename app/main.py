import os
import django
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

app = FastAPI(title="School Management API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Management API"}
