#Read N,Print No of digits in N
n=int(input("Enter a NUmber"))
i=0
while n>0:
    n=n//10
    i+=1
print("Number of digits:",i)