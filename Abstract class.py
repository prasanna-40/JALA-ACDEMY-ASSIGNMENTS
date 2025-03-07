from abc import ABC, abstractmethod  

class AbstractDemo(ABC):  
    def non_abstract(self): print("Non-Abstract Method")  
    @abstractmethod  
    def abstract_method(self): pass  

class SubClass(AbstractDemo):  
    def abstract_method(self): print("Abstract Method Implemented")  
    def call_methods(self):  
        obj = SubClass()  
        obj.abstract_method()  
        obj.non_abstract()  

sub = SubClass()  
sub.non_abstract()  
sub.call_methods()