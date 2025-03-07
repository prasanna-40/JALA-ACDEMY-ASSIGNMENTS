class A:  
    x = 10  
    def f1(self): print("A - f1")  
    def f2(self): print("A - f2")  
    def show(self): print("A - show")  

class B(A):  
    x = 20  
    def f3(self): print("B - f3")  
    def f4(self): print("B - f4")  
    def show(self): print("B - show")  

class C(B):  
    x = 30  
    def f5(self): print("C - f5")  
    def f6(self): print("C - f6")  
    def show(self): print("C - show")  

a, b, c = A(), B(), C()  
for obj in (a, b, c): obj.f1(), obj.f2(), obj.show()  

b.f3(), b.f4()  
c.f5(), c.f6()  

ref = A()  
ref = b; ref.show()  
ref = c; ref.show()  

print(a.x, b.x, c.x)  
ref = b; print(ref.x)  
ref = c; print(ref.x)