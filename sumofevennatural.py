n=int(input("Enter your limit : "))
sum=0
i=1
while(i<=n):
    if(i%2==0):
        sum+=i
    i=i+1
print("Sum of even natural numbers till",n," is : ",sum)