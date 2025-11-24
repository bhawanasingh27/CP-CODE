# You are given two integers A and B. You have to find the value of A^B

A = int(input("Enter base (A): "))
B = int(input("Enter exponent (B): "))

result = 1
i = 1

while i <= B:
    result *= A
    i += 1

print("A^B =", result)
