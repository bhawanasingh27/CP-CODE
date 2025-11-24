# Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N
N = int(input("Enter the number: "))
sum = 0

while N > 0:
    digit = N % 10       
    N = N // 10          
    sum += digit  

print("Sum of digits:", sum)
