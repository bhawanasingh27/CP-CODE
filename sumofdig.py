#Read N,Print sum of digits of N.
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
print("Sum of digits:",sum)