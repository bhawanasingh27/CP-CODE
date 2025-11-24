N = int(input("enter the no :"))
ans =0 
while(N>0):
    digit = N % 10
    ans = ans * 10 + digit
    N //= 10
    
print("the ans is this :",ans)    
