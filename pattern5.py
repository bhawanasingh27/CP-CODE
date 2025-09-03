Row = int(input("Enter number of rows: "))

for i in range(Row, 0, -1):       
    for j in range(i):           
        print("*", end="")
    print()
