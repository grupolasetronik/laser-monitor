


from abc import ABC, abstractmethod
from typing import List
import json

class Topic:
    def __init__(self,key:str,variables:dict):
        self.key:str = key
        self.variables:dict = variables
        self.cache:list = []

    def to_dict(self):
        d = {
                "variables":self.variables,
                "cache":self.cache
            }
        
        return d

    def add_in_cache(self,item:dict):
        self.cache.append(item)
        
    def delete_from_cache_by_key(self,cache_key:str):
        pass
    
    def get_from_cache_by_key(self,cache_key:str) -> dict:
        pass
    
    def update_from_cache_by_key(self,cache_key:str,item:dict):
        pass
    
    def get_cache_items(self,asc:bool) -> List[dict]:
        pass
    
    def clear_cache(self):
        pass
    
    def set_variable(self,key:str):
        pass
    
    def get_variable(self,key:str) -> dict:
        pass
    
    def get_all_variables(self) -> List[dict]:
        pass
    
    def delete_variable(self,key:str):
        pass
    
    def update_variable(self,key:str,value:str):
        pass

class TopicRepository(ABC):
    @abstractmethod
    def get_topic_variables(self,topic:Topic):
        pass
    
    @abstractmethod
    def get_topic_cache(self,topic:Topic):
        pass
    
    @abstractmethod
    def update_topic_variable(self,variable:str,value:str):
        pass
    
    @abstractmethod
    def update_topic_item(self)
    
    
    @abstractmethod
    def create_topic(self,topic:Topic) -> Topic:
        pass
    
    @abstractmethod
    def get_all_topics(self) -> list:
        pass
    
    @abstractmethod
    def delete_topic(self,topic:Topic):
        pass
    
    