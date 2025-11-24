# read n,print number of digits in n
a = int(input("Enter the number: "))
count = 0

if a == 0:   # special case
    count = 1
else:
    while a > 0:
        a = a // 10   # remove last digit
        count += 1

print("Number of digits:", count)
