# print all the divisor and factors of a positive number 
n=int(input("Enter a Number"))
i=1
while(i<=n):
    if(n%i==0):
        print(i)
    i+=1