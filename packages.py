class Class1:  
    def _init_(self): print("Class1 Constructor")  
    def method1(self): print("Method of Class1")  

class Class2:  
    def _init_(self): print("Class2 Constructor")  
    def method2(self): print("Method of Class2")  

from .class1 import Class1  
from .class2 import Class2  

from package1 import Class1  
from package2 import Class2  

obj1 = Class1()  
obj1.method1()  

obj2 = Class2()  
obj2.method2()