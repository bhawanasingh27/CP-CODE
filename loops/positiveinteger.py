# Write a program that takes a positive integer N as input from the user and prints all natural numbers numbers from 1 to N, with each number followed by a space.
N = int(input("Enter a positive integer: "))

for i in range(1, N + 1):
    print(i, end=" ")

