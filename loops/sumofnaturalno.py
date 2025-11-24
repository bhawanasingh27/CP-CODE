# Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from user
n = int(input("enter the no :"))
sum = 0 
i = 0 
while(i <= n):
    sum += i
    
    i += 1
print(sum)