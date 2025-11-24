# Take an integer A as input. You have to print the sum of all odd numbers in the range [1,A].

n = int(input("enter the no :"))
sum = 0 
i = 0 
while(i <= n):
    if i % 2!= 0:
      sum += i
    
    i += 1
print(sum)