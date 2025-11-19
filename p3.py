#factorial of number using recursion
#using recursion print number 1 to n
#using recursion print number n to 1
#write a recursive function to find the nth fabonacci series
def num(n):
    if n==0:
        return
    num(n-1)
    print(n)
n=int(input())
num(n)
