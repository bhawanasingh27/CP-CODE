
n = 5  

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:   # even position → print "*"
            print("*", end=" ")
        else:            # odd position → print odd numbers
            print(j, end=" ")
    print()
