from app.models import InputMessage, RedisQueue
from redis import Redis
class GetRedisQueue:
    
    @staticmethod
    def execute(redis_instance:Redis):
        return RedisQueue(redis_instance)

class PutMessageRedisQueueService:
    @staticmethod
    def execute(
        input_message: InputMessage,
        redis_queue: RedisQueue
    ) -> None:
        redis_queue.put(input_message)