def arithmetic(a, b):  
    print(a + b, a - b, a * b, a / b)  

def inc_dec(x):  
    x += 1  
    print(x)  
    x -= 2  
    print(x)  

def check_equal(a, b):  
    print(a == b)  

def relational(a, b):  
    print(a < b, a <= b, a > b, a >= b)  

def min_max(a, b):  
    print(min(a, b), max(a, b))  

arithmetic(10, 5)  
inc_dec(5)  
check_equal(10, 20)  
relational(15, 10)  
min_max(30, 25)