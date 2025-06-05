from django.db import transaction
from django.contrib.auth.hashers import make_password
from school.models.user import User
from app.schemas.schema import PrincipalCreateRequest

class PrincipalController:

    @staticmethod
    def register_principal(principal_data: PrincipalCreateRequest):
        try:
            with transaction.atomic():
                # Create User
                user = User.objects.create(
                    username=principal_data.username,
                    email=principal_data.email,
                    password=make_password(principal_data.password),
                    first_name=principal_data.first_name,
                    last_name=principal_data.last_name,
                    phone=principal_data.phone,
                    address=principal_data.address,
                    role='PRINCIPAL'
                )

                return {
                    "status": "success",
                    "message": "Principal registered successfully",
                    "principal_id": user.id
                }

        except Exception as e:
            raise Exception(f"Error in registering principal: {str(e)}")
