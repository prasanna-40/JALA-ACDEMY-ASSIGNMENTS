for _ in range(10): print("Bright IT Career")  

i = 1  
while i <= 20: print(i); i += 1  

a, b = 10, 20  
print(a == b, a != b)  

for i in range(1, 21): print(f"{i} Even" if i % 2 == 0 else f"{i} Odd")  

a, b, c = 10, 25, 15  
print(max(a, b, c))  

i = 10  
while i <= 20: print(i); i += 2  

i = 1  
while i <= 10: print(i); i += 1  

n, s, t = 153, 0, 153  
while t: s += (t % 10) ** 3; t //= 10  
print(s == n)  

n, f = 29, 1  
for i in range(2, int(n**0.5) + 1):  
    if n % i == 0: f = 0; break  
print(f)  

n, r = "madam", n[::-1]  
print(n == r)  

def even_odd(n): return {0: "Even", 1: "Odd"}[n % 2]  
print(even_odd(10))  

def gender(c): return {"M": "Male", "F": "Female"}.get(c, "Invalid")  
print(gender("M"))