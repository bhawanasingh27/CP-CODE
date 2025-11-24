# Read three integers and print their maximum
a=int(input("enter a no a :"));
b=int(input("enter a no b :"));
c=int(input("enter a no c :"));
if(a>b and a>c):
    print("a is maximum");
elif(b>c):
    print("b maximum");
else:
    print("c maximum ");