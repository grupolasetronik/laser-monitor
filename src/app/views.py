from datetime import datetime, tzinfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import InputMessageSerializer
from app.models import CustomUser, InputMessage,Topic
from app.services.topic import GetTopicService
from app.services.users import GetUserService
from app.services.input_message import CreateInputMessageService
from app.services.redis_queue import GetRedisQueue,PutMessageRedisQueueService
from app.exceptions.services_exceptions import ServiceException
from app.injection.injection import INJECTION

# Create your views here.

@api_view(["POST"])
def send_message(request):
    serializer = InputMessageSerializer(**request.data)
    if not serializer.is_valid():
        return Response({"detail":serializer.errors})
    try:
        user = GetUserService.execute(user_id=1) #TODO ARRUMAR ISSO
        topic = GetTopicService.execute(topic_key=serializer.topic,user=user)
        input_message = CreateInputMessageService.execute(topic,user,request.data.get("data"))
        redis_queue = GetRedisQueue.execute(INJECTION.redis())
        PutMessageRedisQueueService.execute(input_message,redis_queue)
        
    except ServiceException as e:
        return Response({"detail":f"{e}"})
    return Response(input_message.to_dict())

        
    