from typing import Any
from uuid import UUID
from app.entity.user import User
from app.exceptions.topic_exceptions import WrongTypeException

class Topic:
    def __init__(self,user:User,name:str,description:str,host:Any,topic_uuid:str=None):
        self.__user = user
        self.__name = name
        self.__description = description
        self.__topic_uuid = topic_uuid
        self.__host = host

    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self,value:User):
        if not isinstance(value,User):
            raise WrongTypeException(f"user must be a User entity not {type(value)}")
        self.__user = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value:str):
        if not isinstance(self.__name,str):
            raise WrongTypeException(f"name must be str not {type(value)}")
        self.__name = value

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self,value):
        if not isinstance(self.__name,str):
            raise WrongTypeException(f"description must be str not {type(value)}")
        self.__description = value

    @property
    def topic_uuid(self):
        return self.__topic_uuid
    
    @topic_uuid.setter
    def topic_uuid(self,value:str):
        if not isinstance(self.__name,str):
            raise WrongTypeException(f"description must be str not {type(value)}")
        
        try:
            UUID(value).hex
        except ValueError as e:
            raise WrongTypeException(f"topic_uuid must be str not {type(value)}") from e
        self.__topic_uuid = value

    