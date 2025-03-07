with open("sample.txt", "r") as f: print(f.read())  

with open("output.txt", "w") as f: f.write("Hello, World!")  

with open("output.txt", "r") as f: print(f.read())  

with open("output.txt", "r") as f: print(f.read(5))  

with open("output.txt", "r") as f:  
    f.seek(7)  
    print(f.read())  

import os  
file = "output.txt"  
print(os.access(file, os.R_OK), os.access(file, os.W_OK))