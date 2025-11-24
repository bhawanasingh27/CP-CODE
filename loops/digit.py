# Take an integer N as input and print the count of digits of that number. Input:- N = 10101
n = int(input("enter  the no :"))
count = 0 
while n>0:
    count += 1
    n//=10
print(count)    