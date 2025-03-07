class Parent:  
    def _init_(self, x=0):  
        self.x = x  
        print(f"Parent Constructor: {self.x}")  

class Child(Parent):  
    def _init_(self, y=0):  
        super()._init_(10)  
        self.y = y  
        print(f"Child Constructor: {self.y}")  

class AccessModifiers:  
    def _init_(self): print("Public Constructor")  
    def _protected(self): print("Protected Constructor")  
    def __private(self): print("Private Constructor")  

class AttributesDemo:  
    def _init_(self, name="Default", age=0):  
        self.name = name  
        self.age = age  
        print(f"Name: {self.name}, Age: {self.age}")  

class ConstructorDemo:  
    def _init_(self, a=None, b=None):  
        if a is None and b is None: print("Default Constructor")  
        elif b is None: print(f"One Argument Constructor: {a}")  
        else: print(f"Two Argument Constructor: {a}, {b}")  

ConstructorDemo()  
ConstructorDemo(10)  
ConstructorDemo(10, 20)  

Child(5)  

obj = AccessModifiers()  
obj._protected()  

AttributesDemo("Alice", 25)