
class Normalization:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
    
    def execute(self,raw_dict) -> dict:
        print("1.Normalizado")
       
        #return raw_dict
        return raw_dict
    
    
    
class Validation:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
    
    def execute(self,normalized_dict) -> bool:
        print("2.Validado")
        return True
        

class Condition:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        
    def execute(self) -> bool:
        print("3.Aprovar Execução")
        return True
    

class Execution:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        
    def execute(self) -> None:
        print("4.Executado")
        pass