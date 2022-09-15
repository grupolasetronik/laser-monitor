


from abc import ABC, abstractmethod
from typing import List
import json

class Topic:
    def __init__(self,key:str,variables:dict):
        self.key:str = key
        self.variables:dict = variables
        self.cache:list = []

    def to_dict(self):
    
        return {"variables":self.variables,"cache":self.cache }

    
class TopicRepository(ABC):
    @abstractmethod
    def create_topic(self, topic: Topic) -> Topic:
        pass
    
    @abstractmethod
    def get_all_topics(self):
        pass

    @abstractmethod   
    def delete_topic(self, key: str):
        pass

    @abstractmethod
    def create_variable(self,key_topic:str,key_variable:str,value:str):
        pass
    
    @abstractmethod
    def get_variables(self, key_topic: str, variables_key: List[str]) -> dict:
        pass
    
    @abstractmethod
    def update_variables(self, key_topic: str, variable_key: str, value: dict):
        pass

    @abstractmethod
    def delete_variable(self, key_topic: str, variable_key: str):
        pass
        
    @abstractmethod
    def put_in_cache(self, key_topic: str, item: dict):
        pass

    @abstractmethod
    def get_in_cache(self,key_topic:str,timeout:int):
        pass
