from typing import Any
from app.models import CustomUser, InputMessage, Topic
from app.exceptions.services_exceptions import CreateInputMessageException

class CreateInputMessageService:
    @staticmethod
    def execute(topic:Topic,user:CustomUser,data:Any) -> InputMessage:
        try:
            return InputMessage(topic=topic,user=user,data=data)
        except Exception as e:
            raise CreateInputMessageException(e) from e