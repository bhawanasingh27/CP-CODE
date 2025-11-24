#  Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not
a=int(input("enter a no a :"));
if(a % 5 == 0 and a % 11 == 0):
    print("the no is divisible by both 5 and 11")
else:
    print("the no is not  divisible by both 5 and 11")