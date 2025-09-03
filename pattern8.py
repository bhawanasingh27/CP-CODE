Row = int(input("Enter number of rows: "))

for i in range(1,Row+1):  
    print("*",end=" ")     
    for j in range(Row-i):           
        print("_", end=" ")
    for j in range(i):
        print("*")
    print()
