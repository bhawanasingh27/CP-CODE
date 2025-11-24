# You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A. Even numbers are those numbers that are divisible by 2.

n = int(input("enter the no :"))
sum = 0 
i = 0 
while(i <= n):
    if i % 2 == 0:
      sum += i
    
    i += 1
print(sum)