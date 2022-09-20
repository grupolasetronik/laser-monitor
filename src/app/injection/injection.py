from abc import ABC, abstractmethod
from project.settings import INJECTION
from redis import Redis



class Injection:
    pass

    @abstractmethod
    def redis():
        pass

class TestInjection(Injection):
    
    def redis(self):
        return Redis(password="Quartz")

INJECTION = TestInjection()