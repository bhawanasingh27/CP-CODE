n=int(input("Enter your limits of natural numbers : "))

print("Your even natural numbers are : ")
i=1
while(i<=n):
    if(i%2==0):
        print(i,end=" ")
i=i+1