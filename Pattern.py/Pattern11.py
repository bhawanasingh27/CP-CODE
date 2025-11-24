n = 5  


for i in range(n):
    print("*" * (n - i), end="")            
    print(" " * (2 * i + 1), end="")          
    print("*" * (n - i))                     


for i in range(n):
    print("*" * (i + 1), end="")            
    print(" " * (2 * (n - i) - 1), end="")
    print("*" * (i + 1))                     
