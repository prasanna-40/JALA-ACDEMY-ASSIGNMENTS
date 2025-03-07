class Demo:  
    x = 10  

print(Demo.x)  

d = Demo()  
print(d.x)  

d.x = 20  
print(d.x, Demo.x)  

Demo.x = 30  
print(Demo.x, d.x)