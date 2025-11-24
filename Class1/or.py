num = int(input("Enter a number: "))

if num % 3 == 0 or num % 10 == 4:
    print("The number is divisible by 3 or its last digit is 4.")
else:
    print("The number is not divisible by 3 and its last digit is not 4.")
