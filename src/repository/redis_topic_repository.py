import json
from typing import List
from entity.topic import Topic, TopicRepository
from redis import Redis
###ADICIONAR 
class RedisTopicRepository(TopicRepository):
    def __init__(self,redis_obj:Redis):
        self.redis = redis_obj
        
    def create_topic(self, topic: Topic) -> Topic:
        self.redis.sadd("set:topic",topic.key)
        
    def get_all_topics(self):
        return self.redis.smembers("set:topic")
        
    def delete_topic(self, key: str):
        self.redis.spop("set:topic",key)

    def create_variable(self,key_topic:str,key_variable:str,value:str):
        self.redis.hset(f"hash:variable:{key_topic}",key_variable,value)       
    
    def get_variables(self, key_topic: str, variables_key: List[str]) -> dict:
        return self.redis.hmget(f"hash:variable:{key_topic}",variables_key)
    
    def update_variables(self, key_topic: str, variable_key: str, value: dict):
        self.redis.hmset(f"hash:variable:{key_topic}",variable_key,value)

    def delete_variable(self, key_topic: str, variable_key: str):
        self.redis.hdel(f"hash:variable:{key_topic}",variable_key)
        
    def put_in_cache(self, key_topic: str, item: dict):
        self.redis.rpush(f"queue:cache:{key_topic}",item)

    def get_in_cache(self,key_topic:str,timeout:int):
        return self.redis.blpop(f"queue:cache:{key_topic}",timeout)
    