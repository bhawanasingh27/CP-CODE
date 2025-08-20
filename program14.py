A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if A <= B and A <= C:
    print("Minimum:", A)
elif B <= A and B <= C:
    print("Minimum:", B)
else:
    print("Minimum:", C)
