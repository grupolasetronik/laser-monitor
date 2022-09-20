from django.core.exceptions import ObjectDoesNotExist
from app.models import CustomUser
from app.exceptions.services_exceptions import UserNotFoundException

class GetUserService:
    @staticmethod
    def execute(user_id:str):
        try:
            return CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist as e:
            raise UserNotFoundException(f"User {user_id} does not exists") from e