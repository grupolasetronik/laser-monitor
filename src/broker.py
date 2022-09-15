import json
from multiprocessing import Queue
from importlib.machinery import SourceFileLoader
from entity.topic import TopicRepository, Topic
        

class Broker:
    def __init__(self,queue:Queue,topic_repository:TopicRepository,description=""):
        self.description = description
        #self.queue = queue
        self.db_handler = db_handler
        
    def execute(self):
        
        while True:
            topic = "ipva_relatorio"
            incoming_dict = {"oi":""}
            script_import  = self.__script_import(topic)
            normalized_dict = self.__exec_normalization(script_import,incoming_dict)
            if not self.__exec_validation(script_import,normalized_dict):
                continue
            self.__add_to_cache(topic,validated_dict=normalized_dict)
            if  self.__exec_condition(script_import):
                self.__send_to_execution(script_import)

            
            
    def __script_import(self,topic:str):
        script_import = SourceFileLoader(f"{topic}",f"scripts/{topic}/main.py").load_module()
        return script_import

    def __exec_normalization(self,script_import,incoming_dict):
        return script_import.Normalization().execute(incoming_dict)
    
    def __exec_validation(self,script_import,normalized_dict) -> bool:
        return script_import.Validation().execute(normalized_dict)
    
    def __exec_condition(self,script_import) -> bool:
        return script_import.Condition().execute()
    
    def __send_to_execution(self,script_import):
        return script_import.Execution().execute()
    
    def __add_to_cache(self,topic:str,validated_dict:dict):
        self.db_handler.add_to_cache(topic,validated_dict)
    


if __name__ == "__main__":
    db_handler = DbHandlerJson("db.json")
    b = Broker(db_handler=db_handler)
    b.execute()