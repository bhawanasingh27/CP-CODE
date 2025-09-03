n = int(input("Enter the value of N: "))
for i in range(n,n+1):
    for j in range(1,i+1):
        if (j==1) or (j==n):
            print("*",end="")
        else:
            print("_",end="")
    print()
