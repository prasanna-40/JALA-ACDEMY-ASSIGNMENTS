s1, s2 = "Hello", str("World")  
print(s1 + " " + s2)  
print(len(s1))  
print(s1[1:4])  
print(s1.index("e"))  

import re  
print(bool(re.match(r"Hel.*", s1)))  

print(s1 == s2, s1 < s2, s1 > s2)  
print(s1.startswith("He"), s1.endswith("lo"))  

s3 = "  Python  "  
print(s3.strip())  

print(s1.replace("H", "J"))  
print("a,b,c".split(","))  

n = 100  
print(str(n))  

print(s1.upper(), s1.lower())