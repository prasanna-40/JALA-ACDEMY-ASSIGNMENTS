class MethodOverloading:  
    def method(self, a=None, b=None):  
        if a is None and b is None: print("No Parameters")  
        elif b is None: print(f"One Parameter: {a}")  
        else: print(f"Two Parameters: {a}, {b}")  

    def method_different_types(self, a):  
        if isinstance(a, int): print(f"Integer: {a}")  
        elif isinstance(a, str): print(f"String: {a}")  

    def same_parameters(self, a, b): print(f"Same Parameters: {a}, {b}")  

obj = MethodOverloading()  
obj.method()  
obj.method(10)  
obj.method(10, 20)  

obj.method_different_types(100)  
obj.method_different_types("Hello")  

obj.same_parameters(5, 10)