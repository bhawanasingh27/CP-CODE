# Write a program to input two numbers(A & B) from the user and print the maximum  element among A & B.
A = int(input("Enter first number  "))
B = int(input("Enter second number  "))
if A > B:
    print("Maximum number is A")
elif B > A:
    print("Maximum number is B")
else:
    print("Both numbers are equal.")
