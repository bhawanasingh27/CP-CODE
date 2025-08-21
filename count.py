n=int(input("Enter your digit : "))
c=0
temp=n
i=1
while(n!=0):
    rem=n%10
    c+=1
    n=n//10
    i=i+1
print("Count of digit ",temp," is : ",c)