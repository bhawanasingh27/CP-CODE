Row=int(input("Enter numbr of Row"))
for i in range(1,Row+1):
    for j in range(i+1):
        if(j%2==0):
            print("*",end='')
        else:
            print(j,end='')
    print()
