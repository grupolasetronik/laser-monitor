from uuid import uuid4
from django.core.exceptions import ObjectDoesNotExist
from app.models import CustomUser, Host,Topic
from app.exceptions.services_exceptions import GetTopicServiceException


class CreateTopicService:
    

    @staticmethod
    def execute(
        name:str,
        description:str,
        user:CustomUser,
        host:Host
    ) -> Topic:
        topic_uuid = uuid4().hex

        return Topic.objects.create(
            topic_uuid = topic_uuid,
            name = name,
            description = description,
            user_id = user.id,
            host_id = host.id
        )

class GetTopicService:
    @staticmethod
    def execute(topic_key:str,user:CustomUser):
        try:
            return Topic.objects.get(name=topic_key,user_id=user.id)
        except ObjectDoesNotExist as e:
            try:
                return Topic.objects.get(topic_uuid=topic_key,user_id=user.id)
            except ObjectDoesNotExist as e:
                raise GetTopicServiceException("Topic does not exists") from e
