import json
from entity.topic import Topic, TopicRepository
from redis import Redis

class RedisTopicRepository(TopicRepository):
    def __init__(self,redis_obj:Redis):
        self.redis = redis_obj
        
    def create_topic(self, topic: Topic) -> Topic:
        self.redis.sadd("set:topic",topic.key)
        
    def get_
        
        