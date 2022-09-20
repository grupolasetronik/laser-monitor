from datetime import datetime
from typing import Any
from uuid import uuid4
import pytz
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from redis import Redis
from app.managers import CustomUserManager
from app.models_validators import TopicValidators

# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.localtime())
    user_uuid = models.UUIDField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def get_uuid(self):
        return self.user_uuid

class Host(models.Model):
    user = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    description = models.TextField()
    ip = models.TextField()
    port = models.TextField()    


class Topic(models.Model):
    user = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    #pylint:disable=undefined-variable
    topic_uuid = models.UUIDField(unique=True)
    host = models.ForeignKey(to=Host,on_delete=models.SET_NULL,null=True)
    


class Parameter(models.Model):
    topic = models.ForeignKey(to=Topic,on_delete=models.CASCADE)
    key = models.TextField()
    value = models.TextField()


class InputMessage:
    def __init__(self,topic:Topic,user:CustomUser,data:Any):
        self.__id = None
        self.__topic = topic
        self.__user = user
        self.__data = data
        self.__parameters = []
        self.__created_at = None

    @property
    def id(self):
        if self.__id is None:
            self.__id = uuid4().hex
        return self.__id

    @id.setter
    def id(self,value:str):
        raise NotImplementedError("It is not possible change the message id")

    @property
    def topic(self):
        return self.__topic

    @topic.setter
    def topic(self,value:Topic):
        if not isinstance(value,Topic):
            raise ValueError("topic_id must be a Topic")
        return value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self,value):
        if not isinstance(value,CustomUser):
            raise ValueError("user must be a CustomUser")
        return value

    @property
    def data(self):
        return self.__data

    @property
    def is_valid(self):
        return self.__topic.user.id == self.user.id

    @property
    def created_at(self):
        if self.__created_at is None:
            self.__created_at = timezone.localtime()
        return self.__created_at

    @created_at.setter
    def created_at(self,value:datetime):
        raise NotImplementedError("It is not possible change the message id")

    @property
    def parameters(self):
        return self.__parameters
    
    @parameters.setter
    def parameters(self,value):
        raise NotImplementedError("not allowed to set parameter")


    @property
    def host(self):
        return self.topic.host

    @host.setter
    def host(self,value:Host):
        raise NotImplementedError("not allowed to set host")


    def to_dict(self,to_str=False):
        d = {
            "id":str(self.id),
            "topic":str(self.topic.topic_uuid),
            "data":str(self.data),
            "created_at":str(self.created_at),
        }
        return str(d) if to_str else d

    def to_dict_output(self,to_str=True):
        d = {
            "id":str(self.id),
            "topic":str(self.topic.topic_uuid),
            "data":str(self.data),
            "created_at":str(self.created_at),
            "host":{
                "ip":str(self.topic.host.ip),
                "port":str(self.topic.host.port)
            },
            "parameters":{str(item.key):str(item.value) for item in self.__parameters}
        }
        return str(d) if to_str else d


        

class RedisQueue:
    def __init__(self,redis_instance:Redis):
        self.__redis_instance = redis_instance

    def put(self,input_message:InputMessage):
        _id = input_message.id
        topic_uuid = input_message.topic.topic_uuid
        message = input_message.to_dict_output(True)
    
        self.__redis_instance.hset(f"hash{topic_uuid}",message)
        self.__redis_instance.rpush(f"list{topic_uuid}",_id)

    def get(self,topic_uuid:str):
        message_id = str(self.__redis_instance.rpop(f"list{topic_uuid}"))
        self.__redis_instance.hdel(f"hash{topic_uuid}",message_id)

    def delete(self,topic_uuid:str):
        self.__redis_instance.delete(f"hash{topic_uuid}")
        self.__redis_instance.delete(f"list{topic_uuid}")
    
    def restore(self,topic_uuid:str):
        self.__redis_instance.restore(f"hash{topic_uuid}")
        self.__redis_instance.restore(f"list{topic_uuid}")

